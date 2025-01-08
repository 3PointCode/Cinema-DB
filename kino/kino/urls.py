from django.urls import path

from . import views

urlpatterns = [
    path("", views.repertuar, name="repertuar"),
    path("filmy", views.filmy, name="filmy"),
    path("seans/<int:id>/", views.seans, name="seans"),
    path("rezerwacjaSukces", views.rezerwacjaSukces, name="rezerwacjaSukces"),
]