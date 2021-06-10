from django import forms
from django.forms.widgets import PasswordInput, TextInput
from django.contrib.auth.forms import AuthenticationForm, PasswordResetForm

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=TextInput(attrs={'class':'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))

class BaseSignupForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))

class ContactForm(forms.Form):
    email = forms.EmailField(widget=forms.TextInput(attrs={'class':'form-control'}), required=True)
    subject = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}), required=True)
    message = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control'}), required=True)