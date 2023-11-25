from history.models import QuizHistory as quizH
from useraccount.models import UserAccount
from history.models import ExpiredQuiz
class QuizHistory:
    def __init__(self,StudentId,topic):
        self.StudentId = StudentId
        self.topic = topic

    def get_quiz_history(self):
        login_user = UserAccount.objects.get(studentId = self.StudentId)
        all_quiz_history = quizH.objects.all()
        total_answers = 0
        total_right_answers = 0
        total_wrong_answers = 0
        try:
            for x in all_quiz_history:
                if str(x.user) == str(login_user) and str(x.topic) == str(self.topic):
                    total_answers += 1

                if str(x.user) == str(login_user) and str(x.topic) == str(self.topic) and x.is_correct==True:
                    total_right_answers += 1
                
                if str(x.user) == str(login_user) and str(x.topic) == str(self.topic) and x.is_correct==False:
                    total_wrong_answers += 1
        except:
            pass


        return {'topic':self.topic,'total_answers': total_answers,'total_right_answers':total_right_answers,'total_wrong_answers':total_wrong_answers}
    

class Request_Quiz_History:
    def __init__(self,login_user):
        self.login_user = login_user

    def History(self):
        all_expired_quiz = ExpiredQuiz.objects.all()
        c_user_exp_quiz = []
        all_history = []
        for quiz in all_expired_quiz:
            if quiz.user == self.login_user:
                c_user_exp_quiz.append(quiz.topic)
        for x in c_user_exp_quiz:
            k = QuizHistory(self.login_user,x)
            a= k.get_quiz_history()
            all_history.append(a)
        return all_history


# class QuizStatistics:
#     def __init__(self,StudentId):
#         self.StudentId = StudentId

#     def QStatistics(self):
#         all_quiz_history = quizH.objects.all()
#         right_answer = 0
#         wrong_answer = 0
#         percentage = 0
#         try:
#             for x in all_quiz_history:
#                 if x.user == self.StudentId and x.is_correct == True:
#                     right_answer += 1
#                 elif x.user == self.StudentId and x.is_correct == False:
#                     wrong_answer += 1
#             total_answered = right_answer + wrong_answer
#             percentage = right_answer * 100 / total_answered
#             percentage = int(percentage)
#             return {'right_answer':right_answer,'wrong_answer': wrong_answer,'percentage':percentage}
#         except:
#             pass