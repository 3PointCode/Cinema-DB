from django.shortcuts import render
from django.http import HttpResponse
from .models import Filmy, FilmyKlient, SeansKlient, RezerwacjaKlient

def index(request):
    return HttpResponse("strona glowna")

def repertuar(request):
    filmy = Filmy.objects.all()
    for i in filmy:
        print(i)
    context = {
        'filmy': filmy,
        'message': "hello world"
    }
    return render(request, 'repertuar.html', context)

def filmy(request):
    filmy = RezerwacjaKlient.objects.all().filter(seansid=12)
    context = {
        'filmy': filmy,
        'message': "hello world"
    }
    return render(request, 'filmy.html', context)

def seans(request):
    filmy = Filmy.objects.all()
    for i in filmy:
        print(i)
    context = {
        'filmy': filmy,
        'message': "hello world"
    }
    return render(request, 'filmy.html', context)



    # return HttpResponse("<h1>dsadsa</h1>Hello, world. You're at the polls index.")