from history.models import QuizHistory
from useraccount.models import UserAccount
class RankingHistory:
    def __init__(self,studentId):
        self.studentId = studentId

    def RankingList(self):
        all_quiz_history = QuizHistory.objects.all()
        right_answer = 0
        try:
            c_user = UserAccount.objects.get(studentId=self.studentId)
            for x in all_quiz_history:
                if str(x.user) == str(self.studentId) and x.is_correct == True:
                    right_answer += 1
            return {"studentid": self.studentId,"first_name":c_user.first_name,"last_name":c_user.last_name,"dept":c_user.dept, "right_answer": right_answer}
        except:
            pass

def get_rankinglist():
    ranking_list = []
    all_user = UserAccount.objects.all()
    for x in all_user:
        RH = RankingHistory(x.studentId)
        RL = RH.RankingList()
        ranking_list.append(RL)
    return ranking_list


