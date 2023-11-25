from django.db import models
from useraccount.models import UserAccount
from quiz.models import Category,Question
from django.utils import timezone
# Create your models here.
class QuizHistory(models.Model):
    class Meta:
        verbose_name_plural = 'QUIZ HISTORY'
    user = models.ForeignKey(UserAccount,on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100, blank=True,null=True)
    last_name = models.CharField(max_length=100, blank=True,null=True)
    dept = models.CharField(max_length=100, blank=True,null=True)
    topic = models.ForeignKey(Category, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    ans = models.CharField(max_length=100)
    is_correct = models.BooleanField()
    correct_answer = models.CharField(max_length=100)
    submited_time = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return str(self.user)
    

class ExpiredQuiz(models.Model):
    class Meta:
        verbose_name_plural = 'COMPLETED QUIZ'
    user = models.ForeignKey(UserAccount,on_delete=models.CASCADE)
    topic = models.CharField(max_length=100)
    submited_time = models.DateTimeField(default=timezone.now,editable=False)

    def __str__(self):
        return str(self.user)