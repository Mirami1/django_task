from django.urls import path
from .views import NewsView

app_name = "newsapp_api"

urlpatterns = [
    path('news/', NewsView.as_view()),
    path('news/<int:pk>', NewsView.as_view())
]
