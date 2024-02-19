import json

from django.db.utils import IntegrityError
from django.shortcuts import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.generics import ListAPIView

from users.models import Questions, Tests, User
from users.serializers import QuestionSerializer, TestsSerializer


class TestsListAPIView(ListAPIView):
    serializer_class = TestsSerializer
    authentication_classes = [SessionAuthentication, BasicAuthentication]

    def get_queryset(self):
        school = self.request.query_params.get('school')
        class_number = self.request.query_params.get('class-number')
        print(self.request.user)
        if school and class_number is not None:
            queryset = Tests.objects.filter(school__name=self.request.user.school, number_class__name=self.request.user.number_class)
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
    first_name = request.GET.get('first-name')
    last_name = request.GET.get('last-name')
    surname = request.GET.get('surname')
    email = request.GET.get('email')
    username = request.GET.get('username')
    number_class = request.GET.get('number-class')
    school = request.GET.get('school')
    password = request.GET.get('password')
    try:
        User.objects.create_user(
            username=username,
            email=email,
            password=password,
            first_name=first_name,
            last_name=last_name,
            surname=surname,
            number_class=number_class,
            school=school,
        )
    except (IntegrityError):
        return HttpResponse('Bad')
    return HttpResponse('Success')

