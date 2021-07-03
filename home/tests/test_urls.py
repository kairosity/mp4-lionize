from django.test import SimpleTestCase
from django.urls import reverse, resolve

from home.views import (index, 
                        webdesign, 
                        seo, 
                        social_media_management, 
                        content_creation,
                        admin_dash_products,
                        admin_dash_users,
                        admin_dash_messages)


class TestUrls(SimpleTestCase):

    def test_homepage_url_is_resolved(self):
        url = reverse('home')
        self.assertEquals(resolve(url).func, index)
        
    def test_get_homepage(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home/index.html')

    def test_webdesign_url_is_resolved(self):
        url = reverse('webdesign')
        self.assertEquals(resolve(url).func, webdesign)

    def test_get_webdesign_page(self):
        response = self.client.get('/webdesign')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home/webdesign.html')

    def test_seo_url_is_resolved(self):
        url = reverse('seo')
        self.assertEquals(resolve(url).func, seo)

    def test_get_seo_page(self):
        response = self.client.get('/seo')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home/seo.html')
    
    def test_social_media_management_url_is_resolved(self):
        url = reverse('social-media-management')
        self.assertEquals(resolve(url).func, social_media_management)

    def test_get_social_media_management_page(self):
        response = self.client.get('/social-media-management')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home/social_media_management.html')
    
    def test_content_creation_url_is_resolved(self):
        url = reverse('content-creation')
        self.assertEquals(resolve(url).func, content_creation)

    def test_get_content_creation_page(self):
        response = self.client.get('/content-creation')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home/content_creation.html')

    def test_admin_product_dashboard_url_is_resolved(self):
        url = reverse('admin-dash-products')
        self.assertEquals(resolve(url).func, admin_dash_products)

    def test_get_admin_products_dashboard_page(self):
        response = self.client.get('/admin-product-dashboard')
        self.assertEqual(response.status_code, 302)
        
    def test_admin_user_dashboard_url_is_resolved(self):
        url = reverse('admin-dash-users')
        self.assertEquals(resolve(url).func, admin_dash_users)

    def test_get_admin_user_dashboard_page(self):
        response = self.client.get('/admin-user-dashboard')
        self.assertEqual(response.status_code, 302)

    def test_admin_messages_dashboard_url_is_resolved(self):
        url = reverse('admin-dash-messages')
        self.assertEquals(resolve(url).func, admin_dash_messages)

    def test_get_admin_messages_dashboard_page(self):
        response = self.client.get('/admin-messages-dashboard')
        self.assertEqual(response.status_code, 302)

    