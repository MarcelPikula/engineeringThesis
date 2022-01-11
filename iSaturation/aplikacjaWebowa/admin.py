from django.contrib import admin
from .models import Pomiar, Pacjent


# Register your models here.
@admin.register(Pomiar)
class PomiarAdmin(admin.ModelAdmin):
    list_display = ["number", "nr_pomiaru", "value"]

@admin.register(Pacjent)
class PacjentAdmin(admin.ModelAdmin):
    list_display = ["imie", "nazwisko", "plec"]
