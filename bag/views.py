from django.shortcuts import render

def view_shopping_bag(request):
    '''
    A view to return the shopping bag page.
    '''
    return render(request, 'bag/shopping_bag.html')
