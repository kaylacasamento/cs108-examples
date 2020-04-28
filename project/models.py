from django.db import models
from django.urls import reverse

# Create your models here.

class Cheer(models.Model): # model with the attributes for an athlete
    '''Encapsulate the idea of a cheerleader'''

    # data attributes of a cheerleader:
    first_name = models.TextField(blank=True)
    last_name = models.TextField(blank=True)
    hometown = models.TextField(blank=True)
    class_year = models.TextField(blank=True)
    position = models.TextField(blank=True)
    image_url = models.URLField(blank=True)
    events = models.ForeignKey('Schedule', on_delete="CASCADE")

    def __str__(self): # string representation of the model
        '''Returns a string representation of this object.'''
        return str(self.first_name) + ' ' + str(self.last_name) + ' ' + str(self.hometown) + ' ' + str(self.class_year) + ' ' + str(self.position) + ' ' + str(self.image_url) + ' ' + str(self.events)

    def get_absolute_url(self): # reverse URL
        '''Return a URL to display this cheer object.'''
        return reverse('athlete', kwargs={'pk': self.pk})

class Schedule(models.Model): # model with the attributes of an event in the schedule
    '''Encapsulate the idea of a schedule item'''

    # data attributes of a schedule item:
    date = models.TextField(blank=True)
    time = models.TextField(blank=True)
    event = models.TextField(blank=True)
    location = models.TextField(blank=True)

    def __str__(self): # string representation of the model
        '''Returns a string representation of this object.'''
        return str(self.date) + ' ' + str(self.time) + ' ' + str(self.event) + ' ' + str(self.location)

    def get_absolute_url(self): # reverse URL
        '''Return a URL to display this schedule object.'''
        return reverse('event', kwargs={'pk': self.pk})
