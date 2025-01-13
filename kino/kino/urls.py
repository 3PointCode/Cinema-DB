from django.urls import path

from . import views

urlpatterns = [
    path("", views.repertuar, name="repertuar"),
    path("filmy", views.filmy, name="filmy"),
    path("filmy/<str:tytul>", views.film, name="film"),
    path("seans/<int:id>/", views.seans, name="seans"),
    path("rezerwacjaSukces/<int:id>/<str:seat>/", views.rezerwacjaSukces, name="rezerwacjaSukces"),
]