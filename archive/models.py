from django.db import models

# Create your models here.
class Event(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    event_date = models.DateField()
    location = models.CharField(max_length=100)

    is_upcoming = models.BooleanField(default=False)
    is_previous = models.BooleanField(default=False)

    def __str__(self):
        return self.title

class EventImage(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='images/')
    caption = models.CharField(max_length=100, blank=True)