from django.shortcuts import render,redirect
from django.views import View
from useraccount.models import UserAccount
import random
from .models import *
from history.models import QuizHistory,ExpiredQuiz
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.
class QuizView(LoginRequiredMixin,View):
    def get(self, request, *args, **kwargs):
        login_user = UserAccount.objects.get(id=request.user.id)
        all_category = Category.objects.all()
        all_history = QuizHistory.objects.all()
        all_expired_exam = ExpiredQuiz.objects.all()
        c_user_expired_exam = []


        for x in all_expired_exam:
            if login_user == x.user:
                c_user_expired_exam.append(x.topic)
        
        data = {
            'login_user': login_user,
            'all_category': all_category,
            'all_history': all_history,
            'c_user_expired_exam': c_user_expired_exam,
        }
        return render(request, 'user/quiz.html',context=data)
    

def get_correct_answer(QuestionId):
    all_category = Question.objects.get(uuid=QuestionId).get_answers()
    for ans in all_category:
        if ans['is_correct'] == True:
            return ans['answer']
        else:
            pass

def get_question(request,category):
        if request.method == 'GET':
            login_user = UserAccount.objects.get(id=request.user.id)
            question_objs = list(Question.objects.all())
            req_topic = category
            req_res = []
            random.shuffle((question_objs))
            for question_obj in question_objs:
                if question_obj.category.category_name == str(req_topic):
                    req_res.append({
                        "category_id": question_obj.uuid,
                        "category": question_obj.category.category_name,
                        "question":question_obj.question,
                        "marks": question_obj.marks,
                        "answers": question_obj.get_answers()
                    })
            data = {
                'login_user': login_user,
                'req_res': req_res,
                'req_topic': req_topic,
            }
            return render(request, 'user/question.html',context=data)
        
        if request.method == 'POST':
            req_topic = category
            user = UserAccount.objects.get(id=request.user.id)
            topic = Category.objects.get(category_name = req_topic)
            selected_answers = []
            for question,answer in request.POST.items():
                if question.startswith("teamerror-"):
                    selected_answers.append({
                        "question": question,
                        "answer": answer,
                    })
                    
            for x in selected_answers:
                question_id = x["question"].split("teamerror-")[1]
                question = Question.objects.get(uuid=question_id)
                submitted_ans = x['answer'].split("teamerror-")[0]
                is_correct = False
                currect_ans = get_correct_answer(question_id)
                verify_ans = x['answer'].split("teamerror-")[1]
                if verify_ans == "True":
                    is_correct = True
                else:
                    pass

                exam_history = QuizHistory(user = user,first_name = user.first_name,last_name = user.last_name,dept = user.dept,topic = topic,question = question,ans = submitted_ans,is_correct = is_correct,correct_answer = currect_ans)
                exam_history.save()
            expired_exam = ExpiredQuiz(user = user,topic = topic)
            expired_exam.save()
            return redirect('quiz')