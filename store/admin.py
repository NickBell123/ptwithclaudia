from django.contrib import admin
from .models import *

class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'price',
        'image',
        'digital_good',
        'category',
    )
    ordering = ('name',)

class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )


admin.site.register(Customer)
admin.site.register(Product, ProductAdmin)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(ShippingDetails)
admin.site.register(ProductCategory, ProductCategoryAdmin)