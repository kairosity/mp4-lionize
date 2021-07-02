from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django.contrib import messages
from lionize.validations import (validate_handle, 
                                validate_min_length_2, 
                                validate_phone_number, 
                                validate_min_length_5_phone,
                                )

from django.db.models.signals import post_save
from django.dispatch import receiver
from django_countries.fields import CountryField


class UserProfile(models.Model):
    '''
    A user profile model for maintaining default delivery information and order history. 
    '''
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    default_first_name = models.CharField(max_length=40, null=True, blank=True)
    default_last_name = models.CharField(max_length=60, null=True, blank=True, validators=[validate_min_length_2])
    default_phone_number = models.CharField(max_length=20, null=True, blank=True, validators=[validate_phone_number, validate_min_length_5_phone])
    default_street_address1 = models.CharField(max_length=80, null=True, blank=True)
    default_street_address2 = models.CharField(max_length=80, null=True, blank=True)
    default_town_or_city = models.CharField(max_length=40, null=True, blank=True)
    default_postcode = models.CharField(max_length=20, null=True, blank=True)
    default_county = models.CharField(max_length=80, null=True, blank=True)
    default_country = CountryField(blank_label='Country', null=True, blank=True)
    instagram_handle = models.CharField(max_length=40, null=True, blank=True, validators=[validate_handle])
    linkedin_handle = models.CharField(max_length=40, null=True, blank=True)
    twitter_handle = models.CharField(max_length=40, null=True, blank=True, validators=[validate_handle])
    facebook_handle = models.CharField(max_length=40, null=True, blank=True, validators=[validate_handle])
    consultation = models.BooleanField(default=False)

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
    date = models.DateField(auto_now_add=True)
    resolved = models.BooleanField(default=False)
