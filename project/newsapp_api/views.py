from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response

from newsapp.models import News
from .serializers import NewsSerializer

class NewsView(ListCreateAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer

    def perform_create(self, serializer):
        news_saved = serializer.save()
        return Response({"success": "News '{}' created succesfully".format(news_saved.heading)})


class SingleNewsView(RetrieveUpdateDestroyAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
