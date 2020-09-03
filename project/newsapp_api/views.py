from rest_framework.generics import get_object_or_404
from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from django_filters import rest_framework as filters
from rest_framework.filters import OrderingFilter
from newsapp.models import News,Article
from .serializers import NewsSerializer,ArticleSerializer
from .filters import NewsFilter


class GetArticleView(ListAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer



class GetNewsView(ListAPIView):
    queryset = News.objects.all()
    filter_backends = (filters.DjangoFilterBackend, OrderingFilter)
    filterset_class = NewsFilter
    serializer_class = NewsSerializer
    ordering = ('-update_date',)


class CreateNewsView(APIView):
    def post(self, request):
        news = request.data.get('News')
        serializer = NewsSerializer(data=news)
        if serializer.is_valid(raise_exception=True):
            news_saved = serializer.save()
        return Response({"success": "News '{}' with id='{}' created succesfully".format(news_saved.title, news_saved.id)})


class UpdateNewsView(APIView):
    def put(self, request, pk):
        saved_news = get_object_or_404(News.objects.all(), pk=pk)
        data = request.data.get('News')
        serializer = NewsSerializer(
            instance=saved_news, data=data, partial=True)
        if serializer.is_valid(raise_exception=True):
            news_saved = serializer.save()
        return Response({
            "success": "News '{}' with id='{}' updated successfully".format(news_saved.title, news_saved.id)
        })


class DelNewsView(APIView):
    def delete(self, request, pk):
        news = get_object_or_404(News.objects.all(), pk=pk)
        news.delete()
        return Response({
            "message": "News with id `{}` has been deleted.".format(pk)
        }, status=204)
