from django.urls import path
from .views import eksportuj, nowy_pacjent, wszystkie_pomiary, nowy_obiekt_bd, lista_pacjentow, \
    wybrany_pacjent, usun_pacjenta


urlpatterns = [
    path('home/', wszystkie_pomiary, name="wszystkiepomiary"),
    path('nowyOBD/', nowy_obiekt_bd, name="nowyOBD"),
    path('nowypacjent/', nowy_pacjent, name="nowy_pacjent"),
    path('listapacjentow/', lista_pacjentow, name="lista_pacjentow"),
    path('wybranypacjent/<int:liczba>', wybrany_pacjent, name="wybrany_pacjent"),
    path('usunpacjenta/<int:liczba>', usun_pacjenta, name="usun_pacjenta"),
    path('eksportuj/<int:liczba>', eksportuj, name="eksportuj"),
]

