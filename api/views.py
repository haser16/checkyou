import json

from django.db.utils import IntegrityError
from django.shortcuts import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.generics import ListAPIView

from users.models import Questions, Tests, User
from users.serializers import QuestionSerializer, TestsSerializer


class TestsListAPIView(ListAPIView):
    serializer_class = TestsSerializer

    def get_queryset(self):
        school = self.request.query_params.get('school')
        class_number = self.request.query_params.get('class-number')
        if school and class_number is not None:
            queryset = Tests.objects.filter(school__name=school, number_class__name=class_number)
            return queryset


class QuestionListAPIView(ListAPIView):
    serializer_class = QuestionSerializer

    def get_queryset(self):
        test_id = self.request.query_params.get('test-id')

        if test_id is not None:
            queryset = Questions.objects.filter(test__id=test_id)
            return queryset


@csrf_exempt
def check_answers(request):
    answers = json.loads(request.body)
    questions = Questions.objects.filter(test__id=answers['test_id'])
    answers_user = []
    true_answers = []
    summa = 0
    for item in answers['questions']:
        answers_user.append(answers['questions'][item])

    for item in questions:
        true_answers.append(item.true_answer)

    for answer, true_answers in zip(answers_user, true_answers):
        if answer == true_answers:
            summa += 1

    return HttpResponse(summa)


@csrf_exempt
def registration(request):
    answers = json.loads(request.body)
    try:
        User.objects.create_user(
            username=answers['username'],
            email=answers['email'],
            password=answers['password'],
            first_name=answers['first_name'],
            last_name=answers['last_name'],
            surname=answers['surname'],
            number_class=answers['number_class'],
            school=answers['school'],
        )
        return HttpResponse('Success')
    except (IntegrityError):
        return HttpResponse('Bad')
