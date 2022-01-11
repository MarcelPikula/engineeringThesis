from django.db import models


class Pomiar(models.Model):

    number = models.PositiveSmallIntegerField(blank=False)

    nr_pomiaru = models.PositiveSmallIntegerField(blank=False)

    timestamp = models.CharField(blank=False, max_length=64)

    value = models.PositiveIntegerField(blank=False)

    def __str__(self):
        return self.pomiar()

    def pomiar(self):
        return "Nr ID: {} nr pomiaru {},  czas pomiaru: {}, wartosc: {} ".format(self.number, self.nr_pomiaru,
                                                                                 self.timestamp, self.value)


class Pacjent(models.Model):

    PLEC = {
        (0, 'Kobieta'),
        (1, 'Mezczyzna'),
    }

    imie = models.CharField(max_length=64, blank=False, unique=False)

    nazwisko = models.CharField(max_length=64, blank=False, unique=False)

    data_urodzenia = models.DateField(null=True, blank=False)

    plec = models.PositiveSmallIntegerField(choices=PLEC)

    zdjecie = models.ImageField(upload_to="zdjecia", null=True, blank=True)

    def __str__(self):
        return self.pacjent()

    def pacjent(self):
        return "Imie i nazwisko: {} {} data urodzenia: {} ".format(self.imie, self.nazwisko, self.data_urodzenia)
