from rest_framework import serializers
from .models import Venue, Event, Artist


class ArtistSerializer(serializers.HyperlinkedModelSerializer):
    event = serializers.PrimaryKeyRelatedField(many=True, queryset=Event.objects.all())

    class Meta:
       model = Artist
       fields = ('id', 'name', 'bio', 'genre', 'image_url', 'website_url', 'social_url', 'event')


class EventSerializer(serializers.HyperlinkedModelSerializer):
    venue = serializers.HyperlinkedRelatedField(
        view_name='venue_detail',
        read_only=True
    )

    performing_at = ArtistSerializer(many=True, read_only=True)

    class Meta:
        model = Event
        fields = ('id', 'venue', 'name', 'date', 'start_time', 'end_time', 'description', 'image_url', 'ticket_price', 'performing_at',)


class VenueSerializer(serializers.HyperlinkedModelSerializer):

    event = EventSerializer(many=True, read_only=True)

    venue_url = serializers.ModelSerializer.serializer_url_field(
       view_name='venue_detail'
    )

    class Meta:
       model = Venue
       fields = ('id', 'venue_url', 'name', 'address', 'phone', 'image_url', 'website_url', 'social_url', 'event')


