from django.conf import settings
from django.shortcuts import get_object_or_404
from products.models import Product
from decimal import Decimal


def bag_contents(request):
    '''
    * This function makes the shopping bag contents available universally.
    \n Args:
        request object
    \n Returns:
    * context object including the bag items, the total cost excl. vat, the
    vat total, the grand total & the product count.
    '''
    bag_items = []
    total = 0
    product_count = 0
    bag = request.session.get('bag', {})

    for item_id, quantity in bag.items():
        product = get_object_or_404(Product, pk=item_id)
        total += quantity * product.price
        product_count += quantity
        bag_items.append({
            'item_id': item_id,
            'quantity': quantity,
            'product': product,
        })

    vat = float(total) * 0.23
    grand_total = float(total) + float(vat)

    context = {
        'bag_items': bag_items,
        'total': total,
        'vat_total': vat,
        'grand_total': grand_total,
        'product_count': product_count,
    }

    return context
