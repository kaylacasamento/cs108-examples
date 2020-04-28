# project/urls.py

from django.urls import path
from .views import *

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('roster', RosterPageView.as_view(), name='roster'), # show roster
    path('athlete/<int:pk>', AthletePageView.as_view(), name='athlete'), # show one athlete
    path('schedule', SchedulePageView.as_view(), name='schedule'), # show schedule
    path('schedule/<int:pk>', EventPageView.as_view(), name='event'), # show event
    path('create_athlete', CreateAthleteView.as_view(), name='create_athlete'), # add a new athlete
    path('create_event', CreateEventView.as_view(), name='create_event'), # add a new event
    path('athlete/<int:pk>/update', UpdateAthleteView.as_view(), name='update_athlete'), # update an existing athlete
    path('schedule/<int:pk>/update', UpdateEventView.as_view(), name='update_event'), # update an existing event
    path('athlete/<int:pk>/delete', DeleteAthleteView.as_view(), name='delete_athlete'), # delete an athlete
    path('schedule/<int:pk>/delete', DeleteEventView.as_view(), name='delete_event'), # delete an event


]