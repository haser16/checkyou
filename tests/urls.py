from django.urls import path

from .views import complete_test, test_card, tests

app_name = 'tests'

urlpatterns = [
    path("/<str:school>/<str:class_number>/", tests, name="tests"),
    path("test/<str:name>/<int:id>/", test_card, name="test-card"),
    path("complete-test/<int:success>/", complete_test, name="complete-test"),
]
