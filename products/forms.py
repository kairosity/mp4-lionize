from django import forms
from .widgets import CustomClearableFileInput
from .models import Product, Category

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