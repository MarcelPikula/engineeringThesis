from django.forms import ModelForm
from .models import Pomiar, Pacjent


class PacjentForm(ModelForm):
    class Meta:
        model = Pacjent
        fields = ['imie', 'nazwisko', 'data_urodzenia', 'plec', 'zdjecie']


