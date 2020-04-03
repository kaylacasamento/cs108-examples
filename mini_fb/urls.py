# quotes/urls.py

from django.urls import path
from .views import *
from .forms import *

urlpatterns = [
    # map the URL (empty string) to the function 'homePageView'
    path('', ShowAllProfilesView.as_view(), name='show_all_profiles'),
    path('profile/<int:pk>', ShowProfilePageView.as_view(), name='show_profile_page'), # generic class-base view
    path('create_profile', CreateProfileView.as_view(), name='create_profile'),
    path('profile/<int:pk>/update', UpdateProfileView.as_view(), name="update_profile"), # update
    path('profile/<int:pk>/post_status', create_status_message, name="post_status"),
]