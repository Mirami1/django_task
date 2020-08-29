from django.urls import path
from .views import GetNewsView, PostNewsView, PutNewsView, DelNewsView

app_name = "newsapp_api"

urlpatterns = [
    path('getnews/', GetNewsView.as_view()),
    path('postnews/', PostNewsView.as_view()),
    path('putnews/<int:pk>', PutNewsView.as_view()),
    path('delnews/<int:pk>', DelNewsView.as_view()),

]
