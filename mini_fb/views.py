from django.shortcuts import render

# Create your views here.

from .models import Profile
from django.views.generic import ListView, DetailView

class ShowAllProfilesView(ListView):
    '''Create a subclass of ListView to display all profiles.'''

    model = Profile # retrieve objects of type Facebook from the database
    template_name = 'mini_fb/show_all_profiles.html'
    context_object_name = 'profile_list'

class ShowProfilePageView(DetailView):
    '''Create a class-based view to obtain data for one Profile record'''
    model = Profile
    template_name = 'mini_fb/show_profile_page.html'
    context_object_name = 'show_profile_page'