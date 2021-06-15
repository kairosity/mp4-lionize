from django.db import models
from django.contrib.auth.models import User

from django.db.models.signals import post_save
from django.dispatch import receiver

from django_countries.fields import CountryField


class UserProfile(models.Model):
    '''
    A user profile model for maintaining default delivery information and order history. 
    '''
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    default_phone_number = models.CharField(max_length=20, null=True, blank=True)
    default_street_address1 = models.CharField(max_length=80, null=True, blank=True)
    default_street_address2 = models.CharField(max_length=80, null=True, blank=True)
    default_town_or_city = models.CharField(max_length=40, null=True, blank=True)
    default_postcode = models.CharField(max_length=20, null=True, blank=True)
    default_county = models.CharField(max_length=80, null=True, blank=True)
    default_country = CountryField(blank_label='Country', null=True, blank=True)
    instagram_handle = models.CharField(max_length=40, null=True, blank=True)
    linkedin_handle = models.CharField(max_length=40, null=True, blank=True)
    twitter_handle = models.CharField(max_length=40, null=True, blank=True)
    facebook_handle = models.CharField(max_length=40, null=True, blank=True)
    consultation = models.BooleanField()

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    '''
    Create or update the user profile.
    '''
    if created:
        UserProfile.objects.create(user=instance)
    #Existing users - just save the profile
    instance.userprofile.save()

class Message(models.Model):
    '''
    A Messages model for keeping track of user communication with Lionize.
    '''
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='user_messages')
    subject = models.CharField(max_length=120, null=True, blank=True)
    message = models.TextField(max_length=500, null=True, blank=True)
    date = models.DateField(auto_now=True)
    resolved = models.BooleanField(default=False)
