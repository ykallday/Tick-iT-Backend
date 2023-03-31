from django.db import models

# Create your models here.

class User(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=300)
    email = models.EmailField()
    name = models.CharField(max_length = 200)



class Venue(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    phone = models.CharField(max_length=14)
    image_url = models.TextField(null=True)
    website_url = models.TextField(null=True)
    social_url = models.TextField(null=True)

    def __str__(self):
        return self.name



class Event(models.Model):
    venue = models.ForeignKey(Venue, on_delete=models.CASCADE, related_name='event', default = 0, blank = True)
    name = models.CharField(max_length=200)
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    description = models.TextField()
    image_url = models.TextField()
    ticket_price = models.IntegerField()
    
    
    def __str__(self):
        return self.name



class Artist(models.Model):
    name = models.CharField(max_length = 100)
    bio = models.TextField()
    genre = models.CharField(max_length = 100)
    image_url = models.TextField()
    event = models.ManyToManyField(Event, related_name='performing_at')
    website_url = models.TextField(null=True)
    social_url = models.TextField(null=True)

    def __str__(self):
        return self.name
    

