from django.test import TestCase

class TestViews(TestCase):

    def test_get_homepage(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home/index.html')

    
    def test_get_webdesign_page(self):
        response = self.client.get('/webdesign')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home/webdesign.html')

    
    def test_get_seo_page(self):
        response = self.client.get('/seo')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home/seo.html')

    def test_get_social_media_management_page(self):
        response = self.client.get('/social-media-management')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home/social_media_management.html')

    def test_get_content_creation_page(self):
        response = self.client.get('/social-media-management')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home/social_media_management.html')

        
