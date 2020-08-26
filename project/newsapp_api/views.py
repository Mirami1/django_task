from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from newsapp.models import News
from .serializers import NewsSerializer


class NewsView(APIView):
    def get(self, request):
        news = News.objects.all()
        serializer = NewsSerializer(news, many=True)
        return Response({"News": serializer.data})

    def post(self, request):
        news = request.data.get('News')

        serializer = NewsSerializer(data=news)
        if serializer.is_valid(raise_exception=True):
            news_saved = serializer.save()
        return Response({"success": "News '{}' created succesfully".format(news_saved.heading)})

    def put(self, request, pk):
        saved_news = get_object_or_404(News.objects.all(), pk=pk)
        data = request.data.get('News')
        serializer = NewsSerializer(
            instance=saved_news, data=data, partial=True)
        if serializer.is_valid(raise_exception=True):
            news_saved = serializer.save()
        return Response({
            "success": "News '{}' updated successfully".format(news_saved.heading)
        })

    def delete(self, request, pk):
        # Get object with this pk
        news = get_object_or_404(News.objects.all(), pk=pk)
        news.delete()
        return Response({
            "message": "News with id `{}` has been deleted.".format(pk)
        }, status=204)


