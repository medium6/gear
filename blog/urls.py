from django.urls import path
from .views import showArticles

urlpatterns = [
    path('', showArticles, name='cartoons'),
]