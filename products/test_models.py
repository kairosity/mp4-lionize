from django.test import TestCase
from .models import Product, Category

class TestProductModels(TestCase):

    def setUp(self):
        self.newProduct = Product.objects.create(
            name='seo_audit',
            friendly_name='SEO Audit',
            description='an audit of your current websites seo',
            price=140
        )
    
    def test_model_str(self):
        self.assertEqual(str(self.newProduct), "seo_audit")

    def test_model_friendly_name_str(self):
        self.assertEqual(Product.get_friendly_name(self.newProduct), "SEO Audit")
    
    def test_model_friendly_name_str_is_diff_from_name(self):
        self.assertNotEqual( str(self.newProduct), Product.get_friendly_name(self.newProduct) )

class TestCategoryModels(TestCase):

    def setUp(self):
        self.newCategory = Category.objects.create(name='seo', friendly_name="SEO" )
    
    def test_new_category_created(self):
        self.assertTrue(self.newCategory is not None)