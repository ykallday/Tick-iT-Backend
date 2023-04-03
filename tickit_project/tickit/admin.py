from django.contrib import admin
from .models import Venue, Event, Artist,Ticket
admin.site.register(Venue)
admin.site.register(Event)
admin.site.register(Artist)
admin.site.register(Ticket)
# Register your models here.
