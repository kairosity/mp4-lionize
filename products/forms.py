from django import forms
from .widgets import CustomClearableFileInput
from .models import Product, Review
from categories.models import Category


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
        labels = {
            'category': 'Category:',
            'name': 'Name:',
            'friendly_name': 'Friendly Name:',
            'description': 'Description:',
            'features': 'Features (please separate each feature using a comma , ): ',
            'price': 'Price (€)',
            'current_image': 'Current Image:',
            'image_url': 'Image URL:',
        }

    image = forms.ImageField(label='Image', required=False, widget=CustomClearableFileInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        friendly_names = [(c.id, c.get_friendly_name()) for c in categories]

        self.fields['category'].choices = friendly_names
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['review_title', 'review', 'review_stars']
        labels = {
            'review_title': 'Give your review a title:',
            'review': 'Write your review here:',
            'review_stars': 'From 1 to 5 (1 being a bad rating and 5 being the best) How would you rate this product?',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
                field.widget.attrs['class'] = 'review-form-field'
        
        self.fields['review_stars'].widget = forms.RadioSelect()