from django.contrib import admin
from .models import Genre, Festival, Sponsor, Concert, Concert_on_festival, Ticket, Ticket_for_concert, Band, Artist, Instrument, Genre_and_intruments, Client

admin.site.register(Genre)
admin.site.register(Festival)
admin.site.register(Sponsor)
admin.site.register(Concert)
admin.site.register(Concert_on_festival)
admin.site.register(Ticket)
admin.site.register(Ticket_for_concert)
admin.site.register(Band)
admin.site.register(Artist)
admin.site.register(Instrument)
admin.site.register(Genre_and_intruments)
admin.site.register(Client)