
from .serializers import ArtistSerializer, EventSerializer, VenueSerializer, TicketSerializer
from .models import Venue, Event, Artist,Ticket
from rest_framework import generics
from rest_framework.permissions import AllowAny
# Create your views here.

class VenueList(generics.ListCreateAPIView):
    queryset = Venue.objects.all()
    serializer_class = VenueSerializer

class VenueDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Venue.objects.all()
    serializer_class = VenueSerializer

class EventList(generics.ListCreateAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

class EventDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

class ArtistList(generics.ListCreateAPIView):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer

class ArtistDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer

class TicketList(generics.ListCreateAPIView):
    permission_classes = [AllowAny]
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer

# class TicketDetail(generics.RetrieveUpdateDestroyAPIView):
#     permission_classes = [AllowAny]
#     queryset = Ticket.objects.all()
#     serializer_class = TicketSerializer