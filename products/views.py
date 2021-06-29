from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.db.models.functions import Lower 

from .models import Product, Category
from profiles.models import UserProfile
from .forms import ProductForm, ReviewForm

# Add auth decorators to all these views so that users must be registered and logged in to see them.

@login_required
def all_products(request):
    '''
    A view to show all products.
    '''
    products = Product.objects.filter(in_shop=True)
    query = None

    if request.GET:
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You did not enter a search term.")
                return redirect(reverse('products'))
            
            queries = Q(name__icontains=query) | Q(description__icontains=query) | Q(friendly_name__icontains=query) | Q(features__icontains=query)
            products = products.filter(queries)

            if not products:
                messages.warning(request, "There were no results for your search term.")

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

    products = Product.objects.filter(category__name='web-design', in_shop=True)

    context = {
        'products': products,
    }
    
    return render(request, 'products/web_design.html', context)

@login_required
def seo(request):
    '''
    A view to show all content creation products
    '''

    products = Product.objects.filter(category__name='seo', in_shop=True)

    context = {
        'products': products,
    }

    return render(request, 'products/seo.html', context)

@login_required
def content_creation_products(request):
    '''
    A view to show all content creation products
    '''

    products = Product.objects.filter(category__name='content-creation', in_shop=True)

    context = {
        'products': products,
    }

    return render(request, 'products/content_creation_products.html', context)


@login_required
def social_media_management(request):
    '''
    A view to show all social media management products
    '''

    products = Product.objects.filter(category__name='social-media-management', in_shop=True)

    context = {
        'products': products,
    }

    return render(request, 'products/social_media_management.html', context)


@login_required
def product_detail(request, product_id):
    '''
    A view to show the individual project details.
    '''

    user_purchased_project_and_can_review = False 
    profile = get_object_or_404(UserProfile, user=request.user)
    users_orders = profile.orders.all()
    featured_product_id = product_id
    product = get_object_or_404(Product, pk=product_id)
    category = product.category
    reviews = product.product_reviews.all()
    vat = float((product.price * 23)) * .01
    total_incl_vat = float(product.price) + vat

    # To determine if the logged in user should be allowed to leave a review
    for order in users_orders:
        line_items = order.lineitems.all()
        for item in line_items:
            if item.product.id == featured_product_id:
                if item.reviewed == False:
                    user_purchased_project_and_can_review = True

    # Save form review details on Submit
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = profile
            review.product = product
            review.save()

            # Switch the "reviewed" field from False to True on the order line item
            for order in users_orders:
                line_items = order.lineitems.all()
                for item in line_items:
                    if item.product.id == featured_product_id:
                        item.reviewed = True
                        item.save()
                        break

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
        referring_page_path = referring_page.split('/')[3:]
        
        if len(referring_page_path) > 1:
            referring_page_path1 = referring_page_path[1]
        else:
            referring_page_path1 = None

        context = {
            'product': product,
            'vat': vat,
            'total_incl_vat': total_incl_vat,
            'category': category,
            'referring_page': referring_page,
            'referring_page_path0': referring_page_path[0],
            'referring_page_path1': referring_page_path1,
            'features' : features,
            'user_purchased_product_and_can_review': user_purchased_project_and_can_review,
            'reviews': reviews,
            'form': form,
        }

        return render(request, 'products/product_detail.html', context)


@login_required
def add_product(request):
    """ Add a product to the store """

    if not request.user.is_staff:
        messages.error(request, 'Sorry, but you are not authorized to add new products! If you have an admin account, please login.')
        raise PermissionDenied()

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

    if not request.user.is_staff:
        messages.error(request, 'Sorry, but you are not authorized to edit Lionize products! If you have an admin account, please login.')
        raise PermissionDenied()

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
        messages.error(request, 'Sorry, but you are not authorized to delete Lionize products! If you have an admin account, please login.')
        raise PermissionDenied()

    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    messages.success(request, f'Product "{product.name}" deleted!')
    return redirect(reverse('products'))

@login_required
def remove_from_shop(request, product_id):
    """ Remove a product from being visible in the shop """

    if not request.user.is_staff:
        messages.error(request, 'Sorry, but you are not authorized to remove a product from the Shop! If you have an admin account, please login.')
        raise PermissionDenied()

    product = get_object_or_404(Product, pk=product_id)
    product.in_shop = False
    product.save()
    messages.success(request, f'Product "{product.name}" removed from the shop!')
    return redirect(reverse('admin-dash-products'))

@login_required
def add_to_shop(request, product_id):
    """ Make a product visible in the shop """

    if not request.user.is_staff:
        messages.error(request, 'Sorry, but you are not authorized to alter products! If you have an admin account, please login.')
        raise PermissionDenied()

    product = get_object_or_404(Product, pk=product_id)
    product.in_shop = True
    product.save()
    messages.success(request, f'Product "{product.name}" added to the shop!')
    return redirect(reverse('admin-dash-products'))