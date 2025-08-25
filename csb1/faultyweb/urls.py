from django.urls import path, include

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("notes/", views.notes, name="notes"),
    path("addnote/", views.add_note, name="add_note"),
    path("register/", views.register_view, name="register"),
    path("accounts/", include("django.contrib.auth.urls")),
]