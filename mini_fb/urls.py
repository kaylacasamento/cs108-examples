# quotes/urls.py

from django.urls import path
from .views import ShowAllProfilesView, ShowProfilePageView # our class definition

urlpatterns = [
    # map the URL (empty string) to the function 'homePageView'
    path('', ShowAllProfilesView.as_view(), name='show_all_profiles'),
    path('profile/<int:pk>', ShowProfilePageView.as_view(), name='show_profile_page'), # generic class-base view
]