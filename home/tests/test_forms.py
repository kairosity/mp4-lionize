from django.test import TestCase
from home.forms import ContactForm

class TestContactForm(TestCase):

    def test_subject_is_required(self):
        form = ContactForm({'subject':''})
        self.assertFalse(form.is_valid())
        self.assertIn('subject', form.errors.keys())
