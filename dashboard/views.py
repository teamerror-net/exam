from django.shortcuts import render
from django.views import View
from useraccount.models import UserAccount
from history.models import QuizHistory
from history.cfunction import Request_Quiz_History
from quiz.models import Category,Notice
from ranking.cfunction import get_rankinglist
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.
class DashboardView(LoginRequiredMixin,View):
    def get(self, request, *args, **kwargs):
        login_user = UserAccount.objects.get(id=request.user.id)
        req_history = Request_Quiz_History(login_user)
        all_history = req_history.History()
        all_quiz_history = QuizHistory.objects.all()
        total_participate = len(all_history)
        all_topic = Category.objects.all().count()
        notices = Notice.objects.all()
        labels =[]
        data = []
        for history in all_history:
            labels.append(history['topic'])
            data.append(history['total_right_answers'])
        ranking_list = get_rankinglist()
        sorted_ranking_list = sorted(ranking_list, key=lambda x: x['right_answer'], reverse=True)
        available_exam = all_topic - total_participate
        right_answer = 0
        wrong_answer = 0
        percentage = 0
        try:
            for x in all_quiz_history:
                if x.user == login_user and x.is_correct == True:
                    right_answer += 1
                elif x.user == login_user and x.is_correct == False:
                    wrong_answer += 1
            total_answered = right_answer + wrong_answer
            percentage = right_answer * 100 / total_answered
            percentage = int(percentage)
        except:
            pass
        data = {
            'login_user': login_user,
            'right_answer': right_answer,
            'wrong_answer': wrong_answer,
            'percentage': percentage,
            'all_history': all_history,
            'total_participate': total_participate,
            'all_topic': all_topic,
            'available_exam': available_exam,
            'sorted_ranking_list': sorted_ranking_list,
            'labels': labels,
            'data': data,
            'notices': notices,
        }
        return render(request, 'user/dashboard.html',context=data)