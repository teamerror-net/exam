from django.db import models
import uuid
import random
# Create your models here.
class BaseModel(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4,editable=False)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    class Meta:
        abstract = True

class Category(BaseModel):
    class Meta:
        verbose_name_plural = 'QUIZ TOPIC'
    category_name = models.CharField(max_length=100,verbose_name='Topic')
    description = models.TextField(max_length=500, default="Easy-to-follow video & guides show you how to draw animals, people & more.")
    time = models.IntegerField(default=30)
    
    def __str__(self):
        return (self.category_name)

class Question(BaseModel):
    class Meta:
        verbose_name_plural = 'QUIZ QUESTION'
    category = models.ForeignKey(Category,related_name='category', on_delete=models.CASCADE,verbose_name='Topic')
    question = models.CharField(max_length=100)
    marks = models.IntegerField(default=1,editable=False)

    def __str__(self):
        return self.question
    
    def get_answers(self):
        answer_objs = list(Answer.objects.filter(question = self))
        random.shuffle(answer_objs)
        data = []
        for answer_obj in answer_objs:
            data.append({
                'answer':answer_obj.answer,
                'is_correct': answer_obj.is_correct
            })
        return data

class Answer(BaseModel):
    class Meta:
        verbose_name_plural = 'QUIZ ANSWER'
    question = models.ForeignKey(Question,related_name='questions_answer', on_delete=models.CASCADE)
    answer = models.CharField(max_length=100)
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return self.answer
    


class Notice(models.Model):
    class Meta:
        verbose_name_plural = 'QUICK NOTICE'
    date = models.DateField(auto_now_add=True,editable=False)
    notice = models.TextField(max_length=500)

    def __str__(self):
        return self.notice
    
