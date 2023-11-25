from django.urls import path
from useraccount.views import *
urlpatterns = [
    path('login', LoginView.as_view(),name= 'login'),
    path('signup', SignupView.as_view(),name= 'signup'),
    path('logout', LogoutView.as_view(),name= 'logout'),
]
