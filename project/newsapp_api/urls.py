from django.urls import path
from .views import GetNewsView, CreateNewsView, UpdateNewsView, DelNewsView

app_name = "newsapp_api"

urlpatterns = [
    path('getnews/', GetNewsView.as_view()),
    path('postnews/', CreateNewsView.as_view()),
    path('putnews/<int:pk>', UpdateNewsView.as_view()),
    path('delnews/<int:pk>', DelNewsView.as_view()),

]
