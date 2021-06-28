from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404
from django.contrib import messages 
from django.contrib.auth.decorators import login_required

from products.models import Product

@login_required
def view_shopping_bag(request):
    '''
    A view to return the shopping bag page.
    '''
    return render(request, 'bag/shopping_bag.html')

@login_required
def view_cart(request):
    '''
    View a summary of your shopping bag as a toast.
    '''

    bag = request.session.get('bag', {})

    if len(bag) > 0:
        messages.success(request, f'Here is your current shopping cart:')
    else:
        messages.success(request, f'Your shopping cart is empty.')
    
    request.session['bag'] = bag

    template = request.META['HTTP_REFERER']

    return redirect(template)

@login_required
def add_to_bag(request, item_id):
    '''
    Add a quantity of a specific product to the shopping bag.
    '''

    product = Product.objects.get(pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})

    if item_id in list(bag.keys()):
        bag[item_id] += quantity
        messages.success(request, f'Success! Updated "{product.friendly_name}" order quantity to {bag[item_id]}')
    else:
        bag[item_id] = quantity
        messages.success(request, f'Success! Added {product.friendly_name} to your bag')
    
    request.session['bag'] = bag

    return redirect(request.META['HTTP_REFERER'])

@login_required
def adjust_bag(request, item_id):
    '''
    Adjust the quantity of the specified product. 
    '''
    product = get_object_or_404(Product, pk=item_id)

    quantity = int(request.POST.get('quantity'))
    bag = request.session.get('bag', {})

    if quantity > 0:
        bag[item_id] = quantity
        messages.success(request, f'Updated "{product.friendly_name}" order quantity to {bag[item_id]}')
    else:
        bag.pop(item_id)
        messages.success(request, f'Removed {product.friendly_name} from your bag')
    
    request.session['bag'] = bag
    
    return redirect(reverse('view_shopping_bag'))

@login_required
def remove_from_bag(request, item_id):
    """Remove the item from the shopping bag"""

    product = get_object_or_404(Product, pk=item_id)

    try:
        bag = request.session.get('bag', {})

        bag.pop(item_id)
        messages.success(request, f'Removed {product.friendly_name} from your bag')

        request.session['bag'] = bag
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f'Error removing item: {e}')
        return HttpResponse(status=500)