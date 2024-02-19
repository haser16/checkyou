from django.contrib import auth
from django.shortcuts import HttpResponseRedirect, render, reverse

from .forms import UserLoginForm, UserRegistrationForm


def registration(request):
    if request.method == 'POST':
        form = UserRegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('users:login'))

    form = UserRegistrationForm()
    context = {
        'form': form,
        'title': 'CheckYou - Регистрация',
    }

    return render(request, 'users/registration.html', context)


def login(request):
    context = {
        'title': 'CheckYou - Вход',
    }
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                return HttpResponseRedirect('/')

    form = UserLoginForm()
    context["form"] = form

    return render(request, 'users/login.html', context)


def index(request):
    context = {
        'title': 'CheckYou',
    }
    return render(request, 'users/index.html', context)
