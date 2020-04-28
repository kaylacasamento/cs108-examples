from django.shortcuts import render

# Create your views here.

from .models import Cheer, Schedule # import the Cheer class
from django.views.generic import ListView, DetailView # import the ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .forms import *

class RosterPageView(ListView): # displays the roster page
    '''Create a subclass of ListView to display all athletes.'''

    model = Cheer
    template_name = 'project/roster.html'
    context_object_name = 'all_athletes_list'

class AthletePageView(DetailView): # displays the page for a single athlete
    '''Show the details for one athlete.'''

    model = Cheer
    template_name = 'project/athlete.html'
    context_object_name = 'athlete'

class SchedulePageView(ListView): # displays the schedule page
    '''Create a subclass of ListView to display all events.'''

    model = Schedule
    template_name = 'project/schedule.html'
    context_object_name = 'all_events_list'

class EventPageView(DetailView): # displays the page for a single event
    '''Show the details for one event.'''

    model = Schedule
    template_name = 'project/event.html'
    context_object_name = 'event'

class HomePageView(ListView): # displays the home page
    '''Create a subclass of ListView to display the home page.'''

    model = Cheer # retrieve objects of type Cheer from the database
    template_name = 'project/home.html'
    context_object_name = 'home_page' # how to find the data in the template file

class CreateAthleteView(CreateView): # displays the page to create an athlete
    '''A view to create a new athlete and save it to the database.'''

    form_class = CreateAthleteForm
    template_name = 'project/create_athlete.html'

class CreateEventView(CreateView): # displays the page to create an event
    '''A view to create a new event and save it to the database.'''

    form_class = CreateEventForm
    template_name = 'project/create_event.html'

class UpdateAthleteView(UpdateView): # displays the page to update an existing athlete
    '''A view to update an athlete and save it to the database'''
    form_class = UpdateAthleteForm
    template_name = 'project/update_athlete.html'
    queryset = Cheer.objects.all()

class UpdateEventView(UpdateView): # displays the page to update an existing event
    '''A view to update an event and save it to the database'''
    form_class = UpdateEventForm
    template_name = 'project/update_event.html'
    queryset = Schedule.objects.all()

class DeleteAthleteView(DeleteView): # displays the page to delete an athlete
    '''A view to delete an athlete and remove it from the database.'''
    template_name = 'project/delete_athlete.html'
    queryset = Cheer.objects.all()
    success_url = '../../roster'

class DeleteEventView(DeleteView): # displays the page to delete an event
    '''A view to delete an event and remove it from the database.'''
    template_name = 'project/delete_event.html'
    queryset = Schedule.objects.all()
    success_url = '../../schedule'