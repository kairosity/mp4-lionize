from django.test import TestCase
from profiles.forms import UserProfileForm

class TestUserProfileForm(TestCase):

    def test_no_fields_are_required(self):
        form = UserProfileForm({'default_first_name': ''})
        self.assertTrue(form.is_valid())
