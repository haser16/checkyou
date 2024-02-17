from django.contrib.auth.views import LogoutView
from django.urls import path

from .views import login, registration

app_name = 'users'

urlpatterns = [
    path('registration/', registration, name='registration'),
    path('login/', login, name='login'),
    path("logout/", LogoutView.as_view(), name="logout"),
]
