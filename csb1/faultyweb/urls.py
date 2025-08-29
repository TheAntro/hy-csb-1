from django.urls import path, include

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("notes/", views.notes, name="notes"),
    path("addnote/", views.add_note, name="add_note"),
    path("register/", views.register_view, name="register"),
    path("search/", views.search_notes, name="search"),
    path("accounts/", include("django.contrib.auth.urls")),
]