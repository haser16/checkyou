from django.urls import path

from .views import (QuestionListAPIView, TestsListAPIView, check_answers,
                    registration)

app_name = 'api'

urlpatterns = [
    path("tests/", TestsListAPIView.as_view(), name="tests"),
    path("questions/", QuestionListAPIView.as_view(), name="questions"),
    path("check-answers/", check_answers, name="check-answers"),
    path("check-answers/", check_answers, name="check-answers"),
    path("registration/", registration, name="registration"),
]
