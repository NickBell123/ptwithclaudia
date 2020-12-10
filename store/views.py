from django.shortcuts import render
from .models import *

def store_view(request):
    products = Product.objects.all()
    """ A veiw for the blog posts page """    
    context = {'products': products}
    return render(request, 'store/store.html', context)


def cart_view(request):
    """ A veiw for the blog posts page """
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, order_complete=False)
        items = order.orderitem_set.all()
    else:
        items = []
    context = {
        'items': items,
        'order': order,      
        }
    return render(request, 'store/cart.html', context)


def checkout_view(request):
    """ A veiw for the blog posts page """   
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, order_complete=False)
        items = order.orderitem_set.all()
    else:
        items = []
    context = {
        'items': items,
        'order': order,      
        }
    return render(request, 'store/checkout.html', context)

