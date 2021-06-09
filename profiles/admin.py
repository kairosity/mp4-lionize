from django.contrib import admin
from .models import UserProfile

class UserProfileAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'default_phone_number',
        'default_street_address1',
        'default_street_address2',
        'default_town_or_city',
        'default_postcode',
        'default_county',
        'default_country',
        'instagram_handle',
        'linkedin_handle',
        'twitter_handle',
        'facebook_handle',
    )


admin.site.register(UserProfile, UserProfileAdmin)
