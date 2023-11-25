from django.urls import path
from quiz.views import *
urlpatterns = [
    path('', QuizView.as_view(),name= 'quiz'),
    path('get-question', get_question,name= 'get-question'),
    path('<str:category>', get_question,name= 'get_quiz'),
]
