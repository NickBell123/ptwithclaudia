from django.shortcuts import render
from django.http import JsonResponse
import json
import datetime
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


def processOrder(request):
    transaction_id = datetime.datetime.now().timestamp()
    data = json.loads(request.body)

    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, order_complete=False)
        total = float(data['form']['total'])
        order.transaction_id = transaction_id
        
        if total == float(order.get_cart_total):
            order.complter = True
        order.save()

        if order.shipping == True:
            ShippingDetails.objects.create(
                customer=customer,
                order=order,
                address=data['shipping']['address'],
                city=data['shipping']['city'],
                state=data['shipping']['state'],
                zipcode=data['shipping']['zipcode'],
            )
    else:
        print('uesr is not logged in.')
    return JsonResponse('Item was added', safe=False)