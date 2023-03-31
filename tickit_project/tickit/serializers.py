from rest_framework import serializers
from .models import Venue, Event, Artist


class EventSerializer(serializers.HyperlinkedModelSerializer):
    performing_at = serializers.HyperlinkedRelatedField(
        view_name='artist_detail',
        many=True,
        read_only=True
    )

    venue_id = serializers.PrimaryKeyRelatedField(
        queryset=Venue.objects.all(),
        source='venue'
    )

    class Meta:
        model = Event
        fields = ('id', 'venue', 'venue_id', 'event_name', 'date', 'start_time', 'end_time', 'description', 'image_url', 'ticket_price', 'performing_at')

class ArtistSerializer(serializers.HyperlinkedModelSerializer):
    performing_at = serializers.HyperlinkedRelatedField(
        view_name='event_detail',
        many=True,
        read_only=True
    )
    events = EventSerializer(many=True, read_only=True)

    event_id = serializers.PrimaryKeyRelatedField(
        queryset=Event.objects.all(),
        source='event'
    )
    
    class Meta:
        model = Artist
        fields = ('id', 'event', 'event_id', 'name', 'bio', 'genre', 'image_url', 'performing_at', 'events')



class VenueSerializer(serializers.HyperlinkedModelSerializer):
    event = serializers.HyperlinkedRelatedField(
        view_name='event_detail',
        many=True,
        read_only=True
    )

    venue_url = serializers.ModelSerializer.serializer_url_field(
        view_name='venue_detail'
    )

    class Meta:
        model = Venue
        fields = ('id', 'venue_url', 'name', 'address', 'image_url', 'event')