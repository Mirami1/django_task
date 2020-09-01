from rest_framework.generics import get_object_or_404
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin
from rest_framework.views import APIView
from rest_framework.response import Response
from django_filters import rest_framework as filters
from rest_framework.filters import OrderingFilter
from newsapp.models import News
from .serializers import NewsSerializer


class NewsFilter(filters.FilterSet):
    title = filters.CharFilter(field_name='title', lookup_expr='icontains')

    class Meta:
        model = News
        fields = ['title']


class GetNewsView(ListModelMixin, GenericAPIView):
    queryset = News.objects.all()
    filter_backends = (filters.DjangoFilterBackend, OrderingFilter)
    filterset_class = NewsFilter
    serializer_class = NewsSerializer
    ordering = ('-update_date',)

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class PostNewsView(APIView):
    def post(self, request):
        news = request.data.get('News')
        serializer = NewsSerializer(data=news)
        if serializer.is_valid(raise_exception=True):
            news_saved = serializer.save()
        return Response({"success": "News '{}' with id='{}' created succesfully".format(news_saved.title, news_saved.id)})


class PutNewsView(APIView):
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
