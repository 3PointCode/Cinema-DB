from django.contrib import admin

# Register your models here.

from .models import Filmy, Gatunek, Jezyki, Klienci, Pracownicy, Rezerwacje, Rezyser, Salekinowe, Seanse, Stanowisko, Statusrezerwacji

admin.site.register(Filmy)
admin.site.register(Gatunek)
admin.site.register(Jezyki)
admin.site.register(Klienci)
admin.site.register(Pracownicy)
admin.site.register(Rezerwacje)
admin.site.register(Rezyser)
admin.site.register(Salekinowe)
admin.site.register(Seanse)
admin.site.register(Stanowisko)
admin.site.register(Statusrezerwacji)