from django.shortcuts import render
from django.http import JsonResponse
import json
# from django.views.decorators.csrf import csrf_exempt
from .models import *

def store_view(request):
    products = Product.objects.all()
    """ A veiw for the blog posts page """ 
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, order_complete=False)
        items = order.orderitem_set.all()
        cartTotal = order.get_cart_total
    else:
        items = []
        order = {'get_cart_items':0, 'get_cart_total':0, 'shipping':False}
        cartTotal = order['get_cart_total']
          
    context = {
        'products': products,
        'order': order,
        'cartTotal': cartTotal,
        }
    return render(request, 'store/store.html', context)


def cart_view(request):
    """ A veiw for the blog posts page """
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, order_complete=False)
        items = order.orderitem_set.all()
    else:
        items = []
        order = {'get_cart_items':0, 'get_cart_total':0, 'shipping':False}
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
        cartTotal = order.get_cart_total
    else:
        items = []
        order = {'get_cart_items':0, 'get_cart_total':0, 'shipping':False}
        cartTotal = order['get_cart_total']
    context = {
        'items': items,
        'order': order,      
        }
    return render(request, 'store/checkout.html', context)

# @csrf_exempt
def updateItem(request):
    data = json.loads(request.body)
    productId = data['productID']
    action = data['action']

    print('Product ID:', productId)
    print('Action:', action)

    customer = request.user.customer
    product = Product.objects.get(id=productId)
    order, created = Order.objects.get_or_create(customer=customer, order_complete=False)
    orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)

    if action == 'add':
        orderItem.quantity = (orderItem.quantity + 1)
    elif action == 'sub':
        orderItem.quantity = (orderItem.quantity - 1)
    
    orderItem.save()
    
    if orderItem.quantity <= 0:
        orderItem.delete()
    return JsonResponse('Item was added', safe=False)