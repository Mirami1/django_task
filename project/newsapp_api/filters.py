from django_filters import rest_framework as filters
from rest_framework.filters import OrderingFilter
from newsapp.models import News


class NewsFilter(filters.FilterSet):
    title = filters.CharFilter(field_name='title', lookup_expr='icontains')

    class Meta:
        model = News
        fields = ['title']
