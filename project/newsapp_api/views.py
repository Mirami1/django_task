from rest_framework.generics import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from newsapp.models import News
from .serializers import NewsSerializer


class GetNewsView(APIView):
    def get(self, request):
        get_data = request.query_params.get('title', "")
        news = News.objects.order_by(
                '-creation_date').filter(title__icontains=get_data)
        serializer = NewsSerializer(news, many=True)
        return Response({"News": serializer.data})


class PostNewsView(APIView):
    def post(self, request):
        news = request.data.get('News')
        serializer = NewsSerializer(data=news)
        if serializer.is_valid(raise_exception=True):
            news_saved = serializer.save()
        return Response({"success": "News '{}' with id='{}' created succesfully".format(news_saved.heading, news_saved.id)})


class PutNewsView(APIView):
    def put(self, request, pk):
        saved_news = get_object_or_404(News.objects.all(), pk=pk)
        data = request.data.get('News')
        serializer = NewsSerializer(
            instance=saved_news, data=data, partial=True)
        if serializer.is_valid(raise_exception=True):
            news_saved = serializer.save()
        return Response({
            "success": "News '{}' with id='{}' updated successfully".format(news_saved.heading, news_saved.id)
        })


class DelNewsView(APIView):
    def delete(self, request, pk):
        news = get_object_or_404(News.objects.all(), pk=pk)
        news.delete()
        return Response({
            "message": "News with id `{}` has been deleted.".format(pk)
        }, status=204)
