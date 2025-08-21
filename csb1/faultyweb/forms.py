from django import forms
from django.contrib.auth.models import User

class RegistrationForm(forms.ModelForm):
  class Meta:
    model = User
    widgets = {
        'password': forms.PasswordInput(),
    }
    fields = ('username', 'password')