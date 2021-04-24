from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User


class TestUser(TestCase):

    def setUp(self):
        self.register_url=reverse('account_signup')
        self.login_url=reverse('account_login')
        self.user={
            'email':'testemail@gmail.com',
            'username':'username',
            'password':'password',
            'password2':'password',
            'name':'fullname'
        }
        self.user_short_password={
            'email':'testemail@gmail.com',
            'username':'username',
            'password':'tes',
            'password2':'tes',
            'name':'fullname'
        }

        return super().setUp()

class RegisterTest(TestUser):
    def test_can_view_signup_page(self):
        response=self.client.get(self.register_url)
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response,'account/signup.html')
    
    def test_can_register_user(self):
        response = self.client.post(self.register_url,self.user, format='text/html')
        self.assertEqual(response.status_code, 302)
        
    def test_cant_register_user_withshortpassword(self):
        response=self.client.post(self.register_url,self.user_short_password,format='text/html')
        self.assertEqual(response.status_code,400)
    
    # def test_user_exists(self):
    #     user_count = User.objects.all().count()
    #     self.assertEqual(user_count, 1)
    #     self.assertNotEqual(user_count, 0)
    
    # def test_login(self):
    #     # send login data
    #     response = self.client.post('/accounts/login', self.username, self.password, follow=True)
    #     # should be logged in now
    #     self.assertTrue(response.context['user'].is_active)

    # def test_user_password(self):
    #     self.assertTrue( self.user_a.check_password('laughingGoat123') )

    