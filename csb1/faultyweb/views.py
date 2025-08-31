from datetime import datetime
from django.db import connection
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from .forms import RegistrationForm, NoteForm
from .models import Note

def index(request):
    # A link vulnerable to Host header attack, fix is in settings.py
    login_link = request.build_absolute_uri('/faultyweb/login/')
    return render(request, "faultyweb/index.html", {"login_link": login_link})

# Issue: user authentication is not checked, anyone can access the page if they know the url
# OWASP 2017: Broken access control
# Fix: require user to be logged in
# @login_required()
def notes(request):
    # Issue: notes shows notes from all users, revealing information that the user should not see. 
    # OWASP 2017 Sensitive Data Exposure
    notes = Note.objects.all()
    # Fix: filter notes based on the logged in user
    # notes = Note.objects.filter(user=request.user)
    form = NoteForm
    return render(request, "faultyweb/notes.html", {"form": form, "notes": notes})

@login_required()
def add_note(request):
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            content = form.cleaned_data["content"]
            user = request.user
            date_published = datetime.now()
            note = Note(user=user, content=content, date_published=date_published)
            note.save()
    return redirect("/faultyweb/notes/")

def search_notes(request):
    results = []
    user = request.user
    query = request.GET.get("q")
    if query:
        with connection.cursor() as cursor:
            # Issue: vulnerable for SQL Injection, with e.g. a query like "' OR 1=1 --" returns all notes, not just notes from the user.
            # OWASP 2017 top 10: SQL Injection
            cursor.execute(f"SELECT * FROM faultyweb_note WHERE user_id = { user.id } AND content LIKE '%{query}%'")
            results = cursor.fetchall()
            # Fix: use Django ORM
            # results = Note.objects.filter(user=user, content__icontains=query)
    results = [result[1] for result in results]
    return render(request, "faultyweb/search.html", {"results": results, "query": query})

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
