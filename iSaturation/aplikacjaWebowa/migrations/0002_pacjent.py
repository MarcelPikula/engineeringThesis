# Generated by Django 3.2.9 on 2021-11-23 10:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplikacjaWebowa', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pacjent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imie', models.CharField(max_length=64)),
                ('nazwisko', models.CharField(max_length=64)),
                ('data_urodzenia', models.DateField(null=True)),
                ('plec', models.BooleanField()),
                ('zdjecie', models.ImageField(blank=True, null=True, upload_to='zdjecia')),
            ],
        ),
    ]
