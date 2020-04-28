# project/forms.py

from django import forms
from .models import Cheer, Schedule

class CreateAthleteForm(forms.ModelForm): # form to create a new athlete
    '''A form to add new athletes to the database.'''

    class Meta:
        '''Relates this form to the Cheer model.'''
        model = Cheer # model to use
        fields = ['first_name', 'last_name', 'hometown', 'position', 'image_url', ] # which fields from the model we should use

class CreateEventForm(forms.ModelForm): # form to create a new event
    '''A form to add a new event to the database.'''

    class Meta:
        '''Relates this form to the Schedule model.'''
        model = Schedule # model to use
        fields = ['date', 'time', 'event', 'location', ] # which fields from the model we should use

class UpdateAthleteForm(forms.ModelForm): # form to update an existing athlete
    '''A form to update an athlete to the database'''

    class Meta:
        '''Associate this form with the Cheer model'''
        model = Cheer # model to use
        fields = ['position', 'image_url', ] # which fields from the model we should use

class UpdateEventForm(forms.ModelForm): # form to update an existing event
    '''A form to update an event to the database'''

    class Meta:
        '''Associate this form with the Schedule model'''
        model = Schedule # model to use
        fields = ['date', 'time', 'event', 'location', ] # which fields from the model we should use