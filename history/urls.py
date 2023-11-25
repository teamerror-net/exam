from django.urls import path
from history.views import *
urlpatterns = [
    path('', HistoryView.as_view(),name= 'history'),
]
