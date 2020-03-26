# quotes/urls.py

from django.urls import path
from .views import HomePageView # our class definition

urlpatterns = [
    # map the URL (empty string) to the function 'homePageView'
    path('', HomePageView.as_view(), name='home'), # generic class-base view
]