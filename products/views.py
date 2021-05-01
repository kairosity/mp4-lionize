from django.shortcuts import render, get_object_or_404
from .models import Product

# Add auth decorators to all these views so that users must be registered and logged in to see them.

def all_products(request):
    '''
    A view to show all products.
    '''
    products = Product.objects.all()

    context = {
        'products': products,
    }


    return render(request, 'products/products.html', context)


def webdesign(request):
    '''
    A view to show all web design products
    '''

    products = Product.objects.filter(category__name='web-design')

    context = {
        'products': products,
    }
    
    return render(request, 'products/web_design.html', context)

def seo(request):
    '''
    A view to show all content creation products
    '''

    products = Product.objects.filter(category__name='seo')

    context = {
        'products': products,
    }

    return render(request, 'products/seo.html', context)

def content_creation_products(request):
    '''
    A view to show all content creation products
    '''

    products = Product.objects.filter(category__name='content-creation')

    context = {
        'products': products,
    }

    return render(request, 'products/content_creation_products.html', context)



def product_detail(request, product_id):
    '''
    A view to show the individual project details.
    '''
    product = get_object_or_404(Product, pk=product_id)
    category = product.category

    print(product.id)
    

    context = {
        'product': product,
        'category': category,
    }


    return render(request, 'products/product_detail.html', context)