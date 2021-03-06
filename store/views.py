from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from django.db.models import Q
from django.http import JsonResponse
import json
import datetime
# from django.views.decorators.csrf import csrf_exempt
from .models import *

def store_view(request):
    """ A veiw for the store page to view and sort all products """ 
    products = Product.objects.all()
    query = None
    categories = None
    sort = None
    direction = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if 'direction' in request.GET:
                direction = request.GET['direction']

                if direction == 'desc':
                    sortkey = f'-{sortkey}'
                products = products.order_by(sortkey)

        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = ProductCategory.objects.filter(name__in=categories)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You did not enter search criteria!")
                return redirect(reverse('products'))
            queries = Q(name__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)

    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, order_complete=False)
        items = order.orderitem_set.all()
        cartTotal = order.get_cart_total
    else:
        items = []
        order = {'get_cart_items':0, 'get_cart_total':0, 'shipping':False}
        cartTotal = order['get_cart_total']

    current_sorting = f'{sort}_{direction}'
          
    context = {
        'products': products,
        'order': order,
        'cartTotal': cartTotal,
        'search_term': query,
        'current_categories': categories,
        'current_sorting': current_sorting,
        }
    return render(request, 'store/store.html', context)


def product_view(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    
    context = {
        'product': product,
    }
    return render(request, 'store/product_view.html', context)

def add_to_cart(request, product_id):
    """"""
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    size = None
    if 'product_size' in request.POST:
        size = request.POST['product_size']
    cart = request.session.get('cart', {})

    if size:
        if product_id in list(cart.keys()):
            if size in cart[product_id]['item_by_size'].keys():
                cart[product_id]['item_by_size'][size] += quantity
            else:
                cart[product_id]['item_by_size'][size] = quantity
        else:
            cart[product_id] = {'item_by_size': {size: quantity}}
    else:
        if product_id in list(cart.keys()):
            cart[product_id] += quantity
        else:
            cart[product_id] = quantity

    request.session['cart'] = cart
    return redirect(redirect_url)

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

def update_cart(request, product_id):
    quantity = int(request.POST.get('quantity'))
    size = None
    if 'product_size' in request.POST:
        size = request.POST['product_size']
    cart = request.session.get('cart', {})

    if size:
        if quantity > 0:
            cart[product_id]['item_by_size'][size] = quantity
        else:
            del cart[product_id]['item_by_size'][size]
    else:
        if quantity > 0:
            cart[product_id] = quantity
        else:
            cart.pop(product_id)
    
    request.session['cart'] = cart
    return redirect(reverse('cart'))
    


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