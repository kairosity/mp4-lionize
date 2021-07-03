from django.shortcuts import (render,
                              get_object_or_404,
                              redirect,
                              reverse)
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.db.models.functions import Lower
from django.core.exceptions import PermissionDenied
from .models import Product, Category, Review
from profiles.models import UserProfile
from .forms import ProductForm, ReviewForm


@login_required
def all_products(request):
    '''
    * A view to return all the products for sale.
    * Only available & visible to logged in users.
    \n Args:
    1. request object
    \n Returns:
    * Template displaying all the products listed.
    * If search form is used: returns search results using
    Q object.
    '''
    products = Product.objects.filter(in_shop=True)
    query = None

    if request.GET:
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You did not enter a search term.")
                return redirect(reverse('products'))

            queries = Q(name__icontains=query) | \
                Q(description__icontains=query) | \
                Q(friendly_name__icontains=query) | \
                Q(features__icontains=query)
            products = products.filter(queries)

            if not products:
                messages.warning(request, "There were \
                    no results for your search term.")

    context = {
        'products': products,
        'search_term': query,
    }

    return render(request, 'products/products.html', context)


@login_required
def webdesign(request):
    '''
    * A view to return all the web design products for sale.
    * Only available & visible to logged in users.
    \n Args:
    1. request object
    \n Returns:
    * Template displaying the web design products listed.
    '''

    products = Product.objects.filter(
        category__name='web-design', in_shop=True)

    context = {
        'products': products,
    }

    return render(request, 'products/web_design.html', context)


@login_required
def seo(request):
    '''
    * A view to return all the seo products for sale.
    * Only available & visible to logged in users.
    \n Args:
    1. request object
    \n Returns:
    * Template displaying the seo products listed.
    '''

    products = Product.objects.filter(
        category__name='seo', in_shop=True)

    context = {
        'products': products,
    }

    return render(request, 'products/seo.html', context)


@login_required
def content_creation_products(request):
    '''
    * A view to return all the content creation products for sale.
    * Only available & visible to logged in users.
    \n Args:
    1. request object
    \n Returns:
    * Template displaying the content creation products listed.
    '''

    products = Product.objects.filter(
        category__name='content-creation', in_shop=True)

    context = {
        'products': products,
    }

    return render(request, 'products/content_creation_products.html', context)


@login_required
def social_media_management(request):
    '''
    * A view to return all the social media management
    products for sale.
    * Only available & visible to logged in users.
    \n Args:
    1. request object
    \n Returns:
    * Template displaying the social media management products listed.
    '''

    products = Product.objects.filter(
        category__name='social-media-management', in_shop=True)

    context = {
        'products': products,
    }

    return render(request, 'products/social_media_management.html', context)


@login_required
def product_detail(request, product_id):
    '''
    * A view to return the individual product details.
    * Only available & visible to logged in users.
    \n Args:
    1. request object
    2. product id
    \n Returns:
    * Template displaying the individual product details.
    * Displays the add review form *if* the user can review
    the product in question.
    * Displays all reviews written for this product.
    * If POST: saves the new review to the database &
    updates the reviews listed below.
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

    # To determine if the logged in user
    # should be allowed to leave a review
    for order in users_orders:
        line_items = order.lineitems.all()
        for item in line_items:
            if item.product.id == featured_product_id:
                if item.reviewed is False:
                    user_purchased_project_and_can_review = True

    # Save form review details on Submit
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = profile
            review.product = product
            review.save()

            # Switch the "reviewed" field from False to
            # True on the order line item
            for order in users_orders:
                line_items = order.lineitems.all()
                for item in line_items:
                    if item.product.id == featured_product_id:
                        item.reviewed = True
                        item.save()
                        break

            messages.success(request,
                             'Your review was added successfully!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Failed to add your review. \
                    Please ensure the form is valid.')
    else:
        form = ReviewForm()

        if product.features:
            features = product.features.split(",")
        else:
            features = None

        if request.META['HTTP_REFERER'] is not None:
            referring_page = request.META['HTTP_REFERER']
            referring_page_path = referring_page.split('/')[3:]
        else:
            referring_page = 'none'

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
            'features': features,
            'user_purchased_product_and_can_review':
                user_purchased_project_and_can_review,
            'reviews': reviews,
            'form': form,
        }

        return render(request, 'products/product_detail.html', context)


@login_required
def add_product(request):
    '''
    * Displays the form for adding a new product to the shop.
    * Only available & visible to logged in admin users.
    \n Args:
    1. request object
    \n Returns:
    * POST adds a new product to the shop.
    * GET displays the add product form.
    '''

    if not request.user.is_staff:
        messages.error(request, 'Sorry, but you are not authorized\
            to add new products! If you have an admin account,\
            please login.')
        raise PermissionDenied()

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save(commit=False)
            product.in_shop = True
            product.save()
            messages.success(request, 'Successfully added product!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Failed to add product.\
                Please ensure the form is valid.')
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
    * Displays the form for editing a product.
    * Only available & visible to logged in admin users.
    \n Args:
    1. request object
    2. product id
    \n Returns:
    * POST saves the alterations to the product.
    * GET displays the edit product form.
    '''

    if not request.user.is_staff:
        messages.error(request, 'Sorry, but you are not authorized\
            to edit Lionize products! If you have an admin account,\
            please login.')
        raise PermissionDenied()

    product = get_object_or_404(Product, pk=product_id)
    in_shop = product.in_shop

    if request.method == 'POST':
        form = ProductForm(
            request.POST, request.FILES, instance=product)
        if form.is_valid():
            product_edited = form.save(commit=False)
            product_edited.in_shop = in_shop
            product_edited.save()
            messages.success(request, 'Successfully updated product!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Failed to update product.\
                Please ensure the form is valid.')
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
def edit_review(request, review_id):
    '''
    * Displays the form for editing a review.
    * Only available & visible to logged in users who
    are trying to edit their own review.
    \n Args:
    1. request object
    2. review id
    \n Returns:
    * POST saves the alterations to the review.
    * GET displays the edit review form.
    '''
    review = get_object_or_404(Review, pk=review_id)

    if not request.user.is_authenticated:
        messages.error(request, 'Sorry, but you must be \
            logged in to edit this review!')
        raise PermissionDenied()

    if str(review.user) != str(request.user):
        messages.error(request, "I'm sorry but you cannot edit\
            another user's review!")
        raise PermissionDenied()

    if request.method == 'POST':
        form = ReviewForm(
            request.POST, request.FILES, instance=review)
        if form.is_valid():
            review_edited = form.save()
            messages.success(request, 'Successfully updated review!')
            return redirect(reverse('reviews'))
        else:
            messages.error(request, 'Failed to update review.\
                Please ensure your entries are valid.')
    else:
        form = ReviewForm(instance=review)
        messages.info(request, f'You are editing your review.')

    template = 'profiles/edit_review.html'
    context = {
        'form': form,
        'review': review,
    }

    return render(request, template, context)


@login_required
def delete_product(request, product_id):
    '''
    * Deletes a product from the shop.
    * Only available & visible to logged in superusers.
    \n Args:
    1. request object
    2. product id
    \n Returns:
    * POST deletes the product.
    * GET displays the delete product page.
    '''

    if not request.user.is_superuser:
        messages.error(request, 'Sorry, but you are not authorized\
            to delete Lionize products! If you have an admin account,\
            please login.')
        raise PermissionDenied()

    product = get_object_or_404(Product, pk=product_id)

    if request.method == 'POST':
        product.delete()
        messages.success(request, f'Product "{product.name}" deleted!')
        return redirect(reverse('admin-dash-products'))

    template = 'products/delete_product.html'
    context = {
        'product': product,
    }

    return render(request, template, context)


@login_required
def delete_review(request, review_id):
    '''
    * Deletes a user's review.
    * Only available to logged in users looking to 
    delete their own review.
    \n Args:
    1. request object
    2. review id
    \n Returns:
    * POST deletes the review.
    * GET displays the delete review page.
    '''

    review = get_object_or_404(Review, pk=review_id)
    profile = get_object_or_404(UserProfile, user=request.user)
    users_orders = profile.orders.all()
    product_reviewed_id = review.product.id
    product = get_object_or_404(Product, pk=product_reviewed_id)

    if not request.user.is_authenticated:
        messages.error(request, 'Sorry, but you need to be logged \
        in to your user account in order to delete a review.')
        raise PermissionDenied()

    if str(review.user) != str(request.user):
        messages.error(request, "I'm sorry but you cannot delete\
            another user's review!")
        raise PermissionDenied()

    if request.method == 'POST':
        review.delete()

        # To set that item as not reviewed again.
        for order in users_orders:
            line_items = order.lineitems.all()
            for item in line_items:
                if item.product.id == product_reviewed_id:
                    item.reviewed = False
                    item.save()

        messages.success(request, f'Review for "{review.product.friendly_name}" deleted!')
        return redirect(reverse('reviews'))

    template = 'profiles/delete_review.html'
    context = {
        'review': review,
    }

    return render(request, template, context)



@login_required
def remove_from_shop(request, product_id):
    '''
    * Removes a product from the shop.
    * Only available & visible to logged in admin users.
    \n Args:
    1. request object
    2. product id
    \n Returns:
    * Removes the product from the shop.
    '''

    if not request.user.is_staff:
        messages.error(request, 'Sorry, but you are not authorized\
            to remove a product from the Shop! If you have an admin\
            account, please login.')
        raise PermissionDenied()

    product = get_object_or_404(Product, pk=product_id)
    product.in_shop = False
    product.save()
    messages.success(
        request, f'Product "{product.name}" removed from the shop!')

    return redirect(reverse('admin-dash-products'))


@login_required
def add_to_shop(request, product_id):
    '''
    * Adds the product to the shop.
    * Only available & visible to logged in admin users.
    \n Args:
    1. request object
    2. product id
    \n Returns:
    * Adds the product to the shop.
    '''

    if not request.user.is_staff:
        messages.error(request, 'Sorry, but you are not authorized\
            to alter products! If you have an admin account,\
            please login.')
        raise PermissionDenied()

    product = get_object_or_404(Product, pk=product_id)
    product.in_shop = True
    product.save()
    messages.success(
        request, f'Product "{product.name}" added to the shop!')
    return redirect(reverse('admin-dash-products'))
