from django.db import models

# Create your models here.
class Profile(models.Model):
    '''Models the data attributes of Facebook users'''

    # data attributes of profiles:
    first_name = models.TextField(blank=True)
    last_name = models.TextField(blank=True)
    city = models.TextField(blank=True)
    email_address = models.TextField(blank=True)
    image_url = models.URLField(blank=True)

    def __str__(self):
        '''Returns a string representation of this object.'''
        return str(self.first_name) + ' ' + str(self.last_name) + ' ' + str(self.city) + ' ' + str(self.email_address) + ' ' + str(self.image_url)