from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User


class TestUser(TestCase):

    def setUp(self):
        self.username = 'testuser'
        self.email = 'testinguser@gmail.com'
        self.password = 'comPliCadoP567'


        return super().setUp()

class RegisterTest(TestUser):
    def test_can_view_signup_page(self):
        response=self.client.get(self.register_url)
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response,'account/signup.html')
    
    def test_signup_form(self):
        response = self.client.post(reverse('account_signup'), data={
            'id_username': self.username,
            'id_email': self.email,
            'id_email2': self.email,
            'id_password1': self.password,
            'id_password2': self.password
        })
        self.assertEqual(response.status_code, 200)

    
    def test_is_registered_user(self):
        self.assertEqual(User.objects.all().count(), 1)
        self.assertNotEqual(User.objects.all().count(), 0)
    


    

class LoginTest(TestUser):
    def test_can_access_page(self):
        response=self.client.get(self.login_url)
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response,'account/login.html')

    # def test_login_success(self):

    #     self.client.post(self.register_url, self.user, format='text/html')
    #     user = User.objects.filter(email=self.user['email']).first()
    #     user.is_active=True
    #     user.save()
    #     response= self.client.post(self.login_url, self.user, format='text/html')
    #     self.assertEqual(response.status_code,302)