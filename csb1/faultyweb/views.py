from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User

from .forms import RegistrationForm

def index(request):
    return HttpResponse("Home page")

def register(request):
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
