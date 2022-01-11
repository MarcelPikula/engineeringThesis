from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Pomiar, Pacjent
from .forms import PacjentForm
from django.contrib.auth.decorators import login_required

import json
import csv


@login_required()
def wszystkie_pomiary(request):

    pomiary = Pomiar.objects.all()
    pacjenci = Pacjent.objects.all()

    all_uniq_id = pomiary.values('number').distinct()

    list_of_id = list(all_uniq_id)

    lista_ostatnich_wartosci = []
    for item in list_of_id:
        lista_ostatnich_wartosci.append(Pomiar.objects.filter(number=item['number']).last())

    return render(request, 'home.html', {'pacjenci': pacjenci, 'lista_ostatnich_wartosci': lista_ostatnich_wartosci,
                                         'allUniqId': list_of_id})


def nowy_obiekt_bd(request):
    if request.method == 'POST':
        json_data = json.loads(request.body)
        data = json_data
        new_pomiar = Pomiar(number=data['number'], nr_pomiaru=data['nrPomiaru'], timestamp=data['timestamp'],
                            value=data['value'])
        new_pomiar.save()

        return HttpResponse(200)


@login_required()
def nowy_pacjent(request):
    form = PacjentForm(request.POST or None, request.FILES or None)

    if request.method == 'POST':
        imie = request.POST.get('imie')
        nazwisko = request.POST.get('nazwisko')
        data_urodzenia = request.POST.get('data_urodzenia')
        plec = request.POST.get('plec')
        zdjecie = request.POST.get('zdjecie')

        Pacjent(imie=imie, nazwisko=nazwisko, data_urodzenia=data_urodzenia, plec=plec, zdjecie=zdjecie)

        if form.is_valid():
            form.save()
            return redirect(wszystkie_pomiary)
    return render(request, 'pacjent_form.html', {'form': form, 'button': "Dodaj"})


@login_required()
def lista_pacjentow(request):

    wszyscy_pacjenci = Pacjent.objects.all()

    return render(request, 'lista_pacjentow.html', {'pacjenci': wszyscy_pacjenci, })


@login_required()
def wybrany_pacjent(request, liczba):

    pacjent = list(Pacjent.objects.filter(id=liczba))
    pomiary_dla_wykresu = Pomiar.objects.filter(number=liczba).all()

    x_data_for_chart = []
    y_data_for_chart = []

    for pomiar in pomiary_dla_wykresu:
        x_data_for_chart.append(pomiar.nr_pomiaru)
        y_data_for_chart.append(pomiar.value)
    if not pomiary_dla_wykresu:
        empty_list = 1
    else:
        empty_list = 0

    return render(request, 'wybrany_pacjent.html', {'empty_list': empty_list, 'pacjent': pacjent,
                                                    'x_data_for_chart': x_data_for_chart,
                                                    'y_data_for_chart': y_data_for_chart})


@login_required()
def usun_pacjenta(request, liczba):
    pacjent = get_object_or_404(Pacjent, pk=liczba)

    liczba_pomiarow = Pomiar.objects.filter(number=liczba).all()

    if request.method == "POST":
        pacjent.delete()
        for item in liczba_pomiarow:
            item.delete()
        return redirect(lista_pacjentow)

    return render(request, 'potwierdz.html', {'liczba_pomiarow': liczba_pomiarow, 'pacjent': pacjent})


@login_required()
def eksportuj(request, liczba):
    response = HttpResponse(content_type='text/csv')

    writer = csv.writer(response)
    writer.writerow(['Nr pomiaru', 'Wartosc', 'Czas'])

    for pomiar in Pomiar.objects.filter(number=liczba).all().values_list('nr_pomiaru', 'value', 'timestamp'):
        writer.writerow(pomiar)

    response['Content-Disposition'] = 'attachment; filename = "pomiary.csv"'

    return response
