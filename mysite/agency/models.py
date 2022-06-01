from django.db import models
from django.utils import timezone
import datetime


class Festival(models.Model):
    #  key - code
    code = models.IntegerField(default=0)
    name = models.CharField(max_length=35)
    city = models.CharField(max_length=35)
    country = models.CharField(max_length=35)
    date = models.DateField()
    music_genre = models.CharField(max_length=35)


class Concert(models.Model):
    #  key - number
    number = models.IntegerField(default=0)
    name = models.CharField(max_length=35)
    location = models.CharField(max_length=35)
    time_start = models.DateField()
    time_end = models.TimeField()


class Ticket(models.Model):
    #  key - code
    code = models.IntegerField(default=0)
    price = models.FloatField()
    discount = models.CharField(max_length=35)
    ticket_type = models.CharField(max_length=35)
    ticket_number_sold = models.IntegerField(default=0)
    ticket_number_available = models.IntegerField(default=0)


class Scene(models.Model):
    #  key - id
    id = models.IntegerField(primary_key=True)
    number_of_seats = models.IntegerField(default=0)
    number_of_standing_room = models.IntegerField(default=0)


class Band(models.Model):
    #  key - id
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=35)
    name_of_leader = models.CharField(max_length=35)
    number_of_artists = models.IntegerField(default=0)
    date_of_founding = models.DateField()


class Artist(models.Model):
    #  key - ?
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=35)
    age = models.IntegerField(default=0)
    date_of_birth = models.DateField() 
    years_active = models.IntegerField(default=0)


class Instrument(models.Model):
    #  key - code
    code = models.IntegerField(default=0)
    name = models.CharField(max_length=25)
    producer = models.CharField(max_length=35)


class Genre(models.Model):
    #  key - code
    code = models.IntegerField(default=0)
    name = models.CharField(max_length=25)
    place_of_founding = models.CharField(max_length=35)
    date_of_founding = models.DateField()
