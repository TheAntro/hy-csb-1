from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

from .forms import RegistrationForm

def index(request):
    return render(request, "faultyweb/index.html")

def register_view(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = User.objects.create_user(username, None, password)
            user.save()
            return redirect("/faultyweb")
    else:
        form = RegistrationForm

    return render(request, "faultyweb/register.html", {"form": form})

def login_view(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            pw = form.cleaned_data["password"]
            print(username)
            print(pw)
            user = authenticate(request, username=username, password=pw)
            print(user)
            if user is not None:
                login(request, user)
                return redirect("/faultyweb")
        else:
            print("form not valid!")
    form = RegistrationForm
    return render(request, "faultyweb/login.html", {"form": form})

def logout_view(request):
    logout(request)
    return redirect("/faultyweb")
