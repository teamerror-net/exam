from django.urls import path
from ranking.views import *
urlpatterns = [
    path('', RankingView.as_view(),name= 'ranking'),
]
