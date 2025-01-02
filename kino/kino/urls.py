from django.urls import path

from . import views

urlpatterns = [
    path("aaaa", views.index, name="index"),
]