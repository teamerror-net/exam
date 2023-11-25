from quiz.models import Category,Question
import random
from django.http import HttpResponse


class Start_Quiz:
    def __init__(self,topic):
        self.topic = topic
        self.all_topic = Category.objects.all()
        self.all_question = Question.objects.all()

    def get_topic(self):
        position = None
        for index ,topic in enumerate(self.all_topic):
            if str(topic) == str(self.topic):
                position = index
        requested_topic = self.all_topic[position].category.all()
        for question in requested_topic:
            print(question)

    def get_question(self):
        position = None
        for index ,topic in enumerate(self.all_topic):
            if str(topic) == str(self.topic):
                position = index
        all_requested_question = self.all_topic[position].category.all()
        return all_requested_question

    def get_ans(self,position):
        requested_ans = self.all_question[position].questions_answer.all()
        print(requested_ans)




    def get_quiz(request):
        try:
            question_objs = list(Question.objects.all())
            data = []
            random.shuffle((question_objs))
            for question_obj in question_objs:
                data.append({
                    "category": question_obj.category.category_name,
                    "question":question_obj.question,
                    "marks": question_obj.marks,
                    "answers": question_obj.get_answers()
                })

            return data

        except Exception as e:
            print(e)
        return HttpResponse("Something went wrong")