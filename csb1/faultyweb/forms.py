from django import forms
from django.contrib.auth.models import User
from faultyweb.models import Note

class RegistrationForm(forms.ModelForm):
  class Meta:
    model = User
    widgets = {
        'password': forms.PasswordInput(),
    }
    fields = ('username', 'password')

class NoteForm(forms.ModelForm):
  class Meta:
    model = Note
    fields = ["content"]
