from django.urls import path
from . import views

urlpatterns = [
    path('', views.store_view, name='store'),
    path('cart/', views.cart_view, name='cart'),
    path('product_view/<product_id>', views.product_view, name='product_view'),
    path('add/<product_id>', views.add_to_cart, name='add_to_cart'),
    path('checkout/', views.checkout_view, name='checkout'),
    path('update_cart/<product_id>', views.update_cart, name='update_cart'),
    
    path('checkout/process_order/', views.processOrder, name='process_order'),
]