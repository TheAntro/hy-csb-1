from django.urls import path, include

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("register/", views.register_view, name="register"),
    path("accounts/", include("django.contrib.auth.urls")),
]