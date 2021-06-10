from django import forms
from .models import UserProfile 

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        exclude = ('user','consultation')
        labels = {
            'default_phone_number': 'Phone Number:',
            'default_postcode': 'Postal Code:',
            'default_town_or_city': 'Town or City:',
            'default_street_address1': 'Street Address 1:',
            'default_street_address2': 'Street Address 2:',
            'default_county': 'County, State or Locality:',
            'default_country': 'Country:',
            'instagram_handle' : 'Instagram:',
            'linkedin_handle': 'LinkedIn:',
            'twitter_handle': 'Twitter:',
            'facebook_handle': 'Facebook:',
        }

    def __init__(self, *args, **kwargs):
        '''
        Add placeholders and classes, remove auto-generated labels 
        & set autofocus on the first field
        '''

        super().__init__(*args, **kwargs)
        placeholders = {
            'default_phone_number': 'Phone Number',
            'default_postcode': 'Postal Code',
            'default_town_or_city': 'Town or City',
            'default_street_address1': 'Street Address 1',
            'default_street_address2': 'Street Address 2',
            'default_county': 'County, State or Locality',
            'instagram_handle': 'Instagram',
            'linkedin_handle': 'LinkedIn',
            'twitter_handle': 'Twitter',
            'facebook_handle': 'Facebook',
            
        }

        self.fields['default_phone_number'].widget.attrs['autofocus'] = True 
        for field in self.fields:
            if field != 'default_country':
                if self.fields[field].required:
                    placeholder = f'{placeholders[field]} *'
                else:
                    placeholder = placeholders[field]
                self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'form-class-here'
            # self.fields[field].label = False