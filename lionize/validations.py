from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

# Form Validations

# Last Name must be at least 2 characters long
def validate_min_length_2(value):
    if len(value) < 2:
        raise ValidationError(_('This field must be at least 2 characters long.'), code='invalid')

# Must be a minimum of 50 chars in length
def validate_min_length_50(value):
    if len(value) < 50:
        raise ValidationError(_('This field must be at least 50 characters long.'), code='invalid')

# Phone Number must be at least 5 numbers long
def validate_min_length_5_phone(value):
    if len(value) < 5:
        raise ValidationError(_('This phone number must be at least 5 numbers long.'), code='invalid')

# Phone Number must be a number
def validate_phone_number(value):
    for char in value:
        if char.isalpha():
            raise ValidationError(_('Your phone number must be a number.'), code='invalid')

# Handle Must Include @ symbol
def validate_handle(value):
    if '@' not in value:
        raise ValidationError(_('Your username must include the @ symbol.'), code='invalid')


