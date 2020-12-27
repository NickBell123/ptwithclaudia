from django.urls import path
from . import views

urlpatterns = [
    path('', views.store_view, name='store'),
    path('cart/', views.cart_view, name='cart'),
    path('product_view/<product_id>', views.product_view, name='product_view'),
    path('checkout/', views.checkout_view, name='checkout'),
    path('update_item/', views.updateItem, name='update_item'),
    path('cart/update_item/', views.updateItem, name='update_item'),
    path('checkout/process_order/', views.processOrder, name='process_order'),
]