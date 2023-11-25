from django.contrib import admin
from .models import QuizHistory,ExpiredQuiz
# Register your models here.



class QuizHistoryAdmin(admin.ModelAdmin):

    search_fields = ('topic__category_name','user__studentId')

    list_display = ['user','topic','question','ans', 'is_correct','correct_answer']
    
admin.site.register(QuizHistory,QuizHistoryAdmin)




class ExpiredQuizAdmin(admin.ModelAdmin):

    search_fields = ('topic','user__studentId')

    list_display = ['user','topic',"submited_time"]
    
admin.site.register(ExpiredQuiz,ExpiredQuizAdmin)