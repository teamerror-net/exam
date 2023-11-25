from django.shortcuts import render
from django.views import View
from useraccount.models import UserAccount
from ranking.cfunction import get_rankinglist
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.
class RankingView(LoginRequiredMixin,View):
    def get(self, request, *args, **kwargs):
        login_user = UserAccount.objects.get(id=request.user.id)
        ranking_list = get_rankinglist()
        sorted_ranking_list = sorted(ranking_list, key=lambda x: x['right_answer'], reverse=True)
        data = {
            'login_user': login_user,
            'sorted_ranking_list': sorted_ranking_list,
        }
        return render(request, 'user/ranking.html',context=data)