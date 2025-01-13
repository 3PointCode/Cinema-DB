from django.shortcuts import render
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseRedirect
from .models import Filmy, FilmyKlient, SeansKlient, RezerwacjaKlient, Rezerwacje, Klienci, Seanse, Statusrezerwacji
from .forms import SeatReservationForm
from django.urls import reverse
from django.template import loader
import datetime


def index(request):
    return HttpResponse("strona glowna")

def repertuar(request):
    filmy = FilmyKlient.objects.all()
    for f in filmy:
        seanse = SeansKlient.objects.all().filter(tytul=f.tytul)
        f.seanseFilmu = seanse
    context = {
        'filmy': filmy,
        'templatka': loader.get_template('menu.html').render()
    }
    return render(request, 'repertuar.html', context)

def filmy(request):
    filmy = FilmyKlient.objects.all()
    context = {
        'filmy': filmy,
        'templatka': loader.get_template('menu.html').render()
    }
    return render(request, 'filmy.html', context)

def film(request, tytul):
    film = FilmyKlient.objects.all().filter(tytul=tytul).first()
    context = {
        'film': film,
        'templatka': loader.get_template('menu.html').render()
    }
    return render(request, 'film.html', context)

def seans(request, id):
    if request.method == "POST":
        form = SeatReservationForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            row, column = map(int, form.cleaned_data['seat'].split("-"))
            row += 65
            row = chr(row)
            column += 1
            seatSymbol = str(row) + str(column)
            try:
                seatTaken = RezerwacjaKlient.objects.get(seansid=id, miejsce=seatSymbol)
            except:
                try:
                    client = Klienci.objects.get(email=email)
                except:
                    client = Klienci.objects.create(email=email)
                try:
                    seans = Seanse.objects.get(seansid=id)
                except:
                    return HttpResponseBadRequest("seans not found")

                status = Statusrezerwacji.objects.get(statusid=1)
                rez = Rezerwacje.objects.create(
                    klientid=client,
                    seansid=seans,
                    miejsce=seatSymbol,
                    statusid=status,
                    datazlozenia=datetime.datetime.now()
                )
                url = reverse("rezerwacjaSukces", kwargs={'id': rez.rezerwacjaid, 'seat': seatSymbol})
                return HttpResponseRedirect(url)
            return HttpResponseBadRequest("seat already taken")
        else:
            return HttpResponseBadRequest("invalid form")

    elif request.method == "GET":
        try:
            seansData = SeansKlient.objects.get(seansid=id)
            rezerwacjaData = RezerwacjaKlient.objects.all().filter(seansid=id)
        except:
            return HttpResponseBadRequest()

        form = SeatReservationForm()
        seatData = []
        for seat in rezerwacjaData:
            row = ord(seat.miejsce[0]) - 64
            column = int(seat.miejsce[1:])
            seatData.append( (row-1, column-1) )
        context = {
            'seansData': seansData,
            'seatData': seatData,
            'rowRange': range(10),
            'columnRange': range(20),
            'form': form
        }
        return render(request, 'seans.html', context)
    
def rezerwacjaSukces(request, id = None, seat = None):
    print(id)
    print(seat)
    if id == None or seat == None:
        return HttpResponseRedirect("/kino")
    return render(request, 'rezerwacjaSukces.html', {
        'rezerwacja_id': id,
        'miejsce': seat
    })