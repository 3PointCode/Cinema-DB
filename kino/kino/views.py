from django.shortcuts import render

from django.http import HttpResponse
from .models import Filmy

def index(request):
    filmy = Filmy.objects.all()
    for i in filmy:
        print(i)
    return HttpResponse("<h1>dsadsa</h1>Hello, world. You're at the polls index.")