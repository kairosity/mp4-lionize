from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.db.models.functions import Lower 

from .models import Product, Category
from profiles.models import UserProfile
from .forms import ProductForm, ReviewForm

# Add auth decorators to all these views so that users must be registered and logged in to see them.

def all_products(request):
    '''
    A view to show all products.
    '''
    products = Product.objects.all()
    query = None

    if request.GET:
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You did enter a search term.")
                return redirect(reverse('products'))
            
            queries = Q(name__icontains=query) | Q(description__icontains=query) | Q(friendly_name__icontains=query) | Q(features__icontains=query)
            products = products.filter(queries)

    context = {
        'products': products,
        'search_term': query,
    }


    return render(request, 'products/products.html', context)

@login_required
def webdesign(request):
    '''
    A view to show all web design products
    '''

    products = Product.objects.filter(category__name='web-design')

    context = {
        'products': products,
    }
    
    return render(request, 'products/web_design.html', context)

@login_required
def seo(request):
    '''
    A view to show all content creation products
    '''

    products = Product.objects.filter(category__name='seo')

    context = {
        'products': products,
    }

    return render(request, 'products/seo.html', context)

@login_required
def content_creation_products(request):
    '''
    A view to show all content creation products
    '''

    products = Product.objects.filter(category__name='content-creation')

    context = {
        'products': products,
    }

    return render(request, 'products/content_creation_products.html', context)


@login_required
def social_media_management(request):
    '''
    A view to show all social media management products
    '''

    products = Product.objects.filter(category__name='social-media-management')

    context = {
        'products': products,
    }

    return render(request, 'products/social_media_management.html', context)


@login_required
def product_detail(request, product_id):
    '''
    A view to show the individual project details.
    '''

    user_purchased_project = False 
    profile = get_object_or_404(UserProfile, user=request.user)
    users_orders = profile.orders.all()
    featured_product_id = product_id

    # To determine if the logged in user should be allowed to leave a review
    for order in users_orders:
        line_items = order.lineitems.all()
        for item in line_items:
            if item.product.id == featured_product_id:
                user_purchased_project = True

    product = get_object_or_404(Product, pk=product_id)
    category = product.category
    reviews = product.product_reviews.all()
    vat = float((product.price * 23)) * .01
    total_incl_vat = float(product.price) + vat

    for review in reviews:
        print(review.review_stars)

    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = profile
            review.product = product
            review.save()
            messages.success(request, 'Your review was added successfully!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Failed to add your review. Please ensure the form is valid.')
    else:
        form = ReviewForm()
    
        if product.features:
            features = product.features.split(",")
        else:
            features = None

        referring_page = request.META['HTTP_REFERER']

        context = {
            'product': product,
            'vat': vat,
            'total_incl_vat': total_incl_vat,
            'category': category,
            'referring_page': referring_page,
            'features' : features,
            'user_purchased_product': user_purchased_project,
            'reviews': reviews,
            'form': form,
        }


        return render(request, 'products/product_detail.html', context)


@login_required
def add_product(request):
    """ Add a product to the store """

    if not request.user.is_superuser:
        messages.error(request, 'Sorry but you are not authorized to do that!')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            messages.success(request, 'Successfully added product!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Failed to add product. Please ensure the form is valid.')
    else:
        form = ProductForm()
        
    template = 'products/add_product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)

@login_required
def edit_product(request, product_id):
    '''
    Edit a product in the store.
    '''

    if not request.user.is_superuser:
        messages.error(request, 'Sorry but you are not authorized to edit Lionize products!')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated product!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Failed to update product. Please ensure the form is valid.')
    else:
        form = ProductForm(instance=product)
        messages.info(request, f'You are editing {product.name}')

    template = 'products/edit_product.html'
    context = {
        'form': form,
        'product': product,
    }

    return render(request, template, context)

@login_required
def delete_product(request, product_id):
    """ Delete a product from the store """

    if not request.user.is_superuser:
        messages.error(request, 'Sorry but you are not authorized to do that!')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    messages.success(request, f'Product "{product.name}" deleted!')
    return redirect(reverse('products'))