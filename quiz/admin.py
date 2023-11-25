from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Category)

class AnswerAdmin(admin.StackedInline):
    model = Answer

class QuestionAdmin(admin.ModelAdmin):
    inlines = [AnswerAdmin]
    search_fields = ('category__category_name',)

admin.site.register(Question, QuestionAdmin)
# admin.site.register(Answer)
admin.site.register(Notice)