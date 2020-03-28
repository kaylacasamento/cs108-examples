# quotes/urls.py

from django.urls import path
from .views import ShowAllProfilesView # our class definition

urlpatterns = [
    # map the URL (empty string) to the function 'homePageView'
    path('', ShowAllProfilesView.as_view(), name='show_all_profiles'), # generic class-base view
]