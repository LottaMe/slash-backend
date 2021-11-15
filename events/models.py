from django.db import models
from django.core.exceptions import ValidationError


# Create your models here.
class Event(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=1000)
    extract = models.CharField(max_length=150)
    start = models.DateTimeField()
    end = models.DateTimeField()
    max_participants = models.PositiveIntegerField()
    participants = models.ManyToManyField('users.CustomUser', blank=True)
    def __str__(self):
        return self.title

    def clean(self):
        super().clean()
        if not ((self.start <= self.end)):
            raise ValidationError('Invalid start and end datetime')
    class Meta:
        abstract = True

class Hackathon(Event):
    internal = models.BooleanField(default=False)

class Workshop(Event):
    organizer = models.CharField(max_length=150)
    hackathon = models.ForeignKey(Hackathon, related_name='workshops', on_delete=models.CASCADE)