from django.shortcuts import render
from django.views import View
from useraccount.models import UserAccount
from quiz.models import Category
from history.cfunction import Request_Quiz_History
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.
class HistoryView(LoginRequiredMixin,View):
    def get(self, request, *args, **kwargs):
        login_user = UserAccount.objects.get(id=request.user.id)
        all_categories = Category.objects.all()
        req_history = Request_Quiz_History(login_user)
        all_history = req_history.History()
        data = {
            'login_user': login_user,
            'all_categories': all_categories,
            'all_history': all_history,
        }
        return render(request, 'user/history.html',context=data)