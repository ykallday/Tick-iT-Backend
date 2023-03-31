from django.db import models

# Create your models here.
class Venue(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    image_url = models.TextField()

    def __str__(self):
        return self.name



class Event(models.Model):
    venue = models.ForeignKey(Venue, on_delete=models.CASCADE, related_name='event', blank = True)
    event_name = models.CharField(max_length=200)
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    description = models.TextField()
    image_url = models.TextField()
    ticket_price = models.IntegerField()
    
    def __str__(self):
        return self.event_name



class Artist(models.Model):
    name = models.CharField(max_length = 100)
    bio = models.TextField()
    genre = models.CharField(max_length = 100)
    image_url = models.TextField()
    event = models.ManyToManyField(Event, related_name='performing_at')

    def __str__(self):
        return self.name


