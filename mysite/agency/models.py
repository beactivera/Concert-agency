import datetime
from django.urls import reverse
from django.db import models
from django.utils import timezone


class Genre(models.Model):
    code = models.IntegerField(default=0)
    name = models.CharField(max_length=25)
    place_of_founding = models.CharField(max_length=35)
    date_of_founding = models.DateField()


class Festival(models.Model):
    music_genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    code = models.IntegerField(default=0)
    name = models.CharField(max_length=35, unique=True, blank=False)
    city = models.CharField(max_length=35)
    country = models.CharField(max_length=35)
    date = models.DateField()


class Sponsor(models.Model):
    code = models.IntegerField(default=0)
    name = models.CharField(max_length=25)


class Concert(models.Model):
    number = models.IntegerField(default=0)
    name = models.CharField(max_length=35)
    scene_name = models.CharField(max_length=35, blank=True, default="")
    location = models.CharField(max_length=35)
    date = models.DateField()


class Concert_on_festival(models.Model):
    festival_id = models.ForeignKey(Festival, on_delete=models.CASCADE)
    concert_id = models.ForeignKey(Concert, on_delete=models.CASCADE)


class Ticket(models.Model):
    code = models.IntegerField(default=0)
    price = models.FloatField()
    discount = models.CharField(max_length=35)
    ticket_type = models.CharField(max_length=35)
    ticket_number_sold = models.IntegerField(default=0)
    ticket_number_available = models.IntegerField(default=0)


class Ticket_for_concert(models.Model):
    ticket_id = models.ForeignKey(Ticket, on_delete=models.CASCADE)
    concert_id = models.ForeignKey(Concert, on_delete=models.CASCADE)


# class Scene(models.Model):
#     #  key - id
#     id = models.IntegerField(primary_key=True)
#     number_of_seats = models.IntegerField(default=0)
#     number_of_standing_room = models.IntegerField(default=0)


class Band(models.Model):
    id = models.IntegerField(primary_key=True, default="")
    name = models.CharField(max_length=35)
    name_of_leader = models.CharField(max_length=35)
    number_of_artists = models.IntegerField(default=0)
    date_of_founding = models.DateField()


class Artist(models.Model):
    band_id = models.ForeignKey(Band, on_delete=models.CASCADE, blank=True, null=True)
    genre_id = models.ForeignKey(Genre, on_delete=models.CASCADE, blank=True, null=True)
    nickname = models.CharField(max_length=25, unique=True, default="")
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=35)
    age = models.IntegerField(default=0)
    date_of_birth = models.DateField()
    years_active = models.IntegerField(default=0)


class Instrument(models.Model):
    code = models.IntegerField(default=0)
    name = models.CharField(max_length=25)
    producer = models.CharField(max_length=35)


class Genre_and_intruments(models.Model):
    genre_id = models.ForeignKey(Genre, on_delete=models.CASCADE)
    intrument_id = models.ForeignKey(Instrument, on_delete=models.CASCADE)


class Client(models.Model):
    name = models.CharField(max_length=32)
    surname = models.CharField(max_length=32)
    login = models.CharField(max_length=64, unique=True, default="")
    email = models.EmailField(unique=True, blank=False, default="")
    phone_number = models.CharField(max_length=23, unique=True, blank=True)

    def __str__(self):
        return str(
            str(self.name) + " " + str(self.surname) + " Tel: " + str(self.phone_number) + " E-mail: " + str(self.email)
        )


    def get_login(self):
        return self.login


    def get_email(self):
        return self.email
