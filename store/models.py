from django.db import models
from django.contrib.auth.models import User

class ProductCategory(models.Model):

    class Meta:
        verbose_name_plural = 'Product Categories'

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=50, null=True)
    email = models.EmailField(null=True)
    
    def __str__(self):
        return self.name



class Product(models.Model):
    name = models.CharField(max_length=254)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    description = models.TextField()
    has_sizes = models.BooleanField(default=False, null=True, blank=True)
    image = models.ImageField(null=True, blank=True, upload_to="product_images/")
    digital_good = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    


class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, blank=True, null=True)
    order_date = models.DateTimeField(auto_now_add=True)
    order_complete = models.BooleanField(default=False, null=True, blank=False)
    transaction_id = models.CharField(max_length=50, null=True)

    @property
    def get_cart_total(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.get_total for item in orderitems])
        return total

    @property
    def get_cart_items(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.quantity for item in orderitems])
        return total

    def __str__(self):
        return str(self.id)


class OrderItem(models.Model):
    order = models.ForeignKey(Order, null=True, blank=False,
                              on_delete=models.SET_NULL)
    product = models.ForeignKey(Product, null=True, blank=False,
                                on_delete=models.SET_NULL)
    product_size = models.CharField(max_length=2, null=True,
                                    blank=True)  
    quantity = models.IntegerField(null=False, blank=False, default=0)
    
    date_added = models.DateTimeField(auto_now_add=True)

    @property
    def get_total(self):
        total = self.quantity * self.product.price
        return total



class ShippingDetails(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, blank=True, null=True)
    order = models.ForeignKey(Order, null=False, blank=False,
                              on_delete=models.CASCADE,
                              related_name='shipping_details')
    address = models.CharField(max_length=254)
    city = models.CharField(max_length=54)
    state = models.CharField(max_length=54)
    zipcode = models.CharField(max_length=25)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.address