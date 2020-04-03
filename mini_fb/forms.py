from django import forms
from .models import Profile, StatusMessage

class CreateProfileForm(forms.ModelForm):
    '''A form to add new Profiles to the database.'''

    class Meta:
        '''Relates this form to the Profile model.'''
        model = Profile
        fields = ['first_name', 'last_name', 'city', 'email_address', 'image_url', ] # which fields from model we should use

class UpdateProfileForm(forms.ModelForm):
    '''A form to update a profile to the database.'''

    class Meta:
        '''Associate this form with the Profile model.'''
        model = Profile
        fields = ['city', 'email_address', 'image_url', ] # which fields from model we can update

class CreateStatusMessageForm(forms.ModelForm):
    '''A form to update a profile's status to the database.'''

    class Meta:
        '''Associate this form with the StatusMessage model.'''
        model = StatusMessage
        fields = ['message', ] # which fields from model we can update