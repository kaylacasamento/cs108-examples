from django.contrib import admin

# Register your models here.
from .models import Cheer, Schedule
admin.site.register(Cheer)
admin.site.register(Schedule)