from django.db import models
from django.urls import reverse

# Create your models here.
class Profile(models.Model):
    '''Models the data attributes of Facebook users'''

    # data attributes of profiles:
    first_name = models.TextField(blank=True)
    last_name = models.TextField(blank=True)
    city = models.TextField(blank=True)
    email_address = models.TextField(blank=True)
    image_url = models.URLField(blank=True)
    friends = models.ManyToManyField("self")

    def __str__(self):
        '''Returns a string representation of this object.'''
        return str(self.first_name) + ' ' + str(self.last_name) + ' ' + str(self.city) + ' ' + str(self.email_address) + ' ' + str(self.image_url)

    def get_status_messages(self):
        '''Return a QuerySet of all quotes for this person'''
        status = StatusMessage.objects.filter(profile=self.pk)
        return status

    def get_absolute_url(self):
        '''Return a URL to display this quote object.'''
        return reverse("show_profile_page", kwargs={"pk":self.pk})

    def get_friends(self):
        '''Return a QuerySet of all friends for this person.'''
        friend_list = Profile.objects.filter(friends=self.pk)
        return friend_list

    def get_news_feed(self):
        '''Obtains and returns the news feed items'''
        friends = self.get_friends()
        friends_news = Profile.objects.filter(profile=friends.pk)
        my_news = Profile.objects.filter(profile=self.pk)
        queryset = friends | my_news
        news = StatusMessage.objects.filter(profile__in = concatenated_querysets).order_by("-timestamp")
        return news

    def get_friend_suggestions(self):
        '''Return a QuerySet of friend suggestions for the Profile'''
        possible_friends = Profile.objects.all().exclude(pk__in=self.get_friends())
        return possible_friends

class StatusMessage(models.Model):
    '''Models the data attributes of Facebook status message'''

    timestamp = models.DateTimeField(auto_now_add=True)
    message = models.TextField(blank=True)
    image = models.ImageField(blank=True)
    profile = models.ForeignKey('profile', on_delete=models.CASCADE)

    def __str__(self):
        '''Returns a string representation of this object'''
        return '%s %s %s' % (self.timestamp, self.message, self.image)