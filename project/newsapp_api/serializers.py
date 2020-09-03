from rest_framework import serializers

from newsapp.models import News, Article


class NewsSerializer(serializers.ModelSerializer):

    class Meta:
        model = News
        fields = ('id', 'title', 'description', 'creation_date', 'update_date')


class ArticleSerializer(serializers.ModelSerializer):
    news = NewsSerializer(many=True)

    class Meta:
        model = Article
        fields = ('id', 'title', 'description',
                  'creation_date', 'update_date', 'news')
