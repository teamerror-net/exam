from django.urls import path
from usersettings.views import *
urlpatterns = [
    path('', UserSettingsView.as_view(),name= 'settings'),
]
