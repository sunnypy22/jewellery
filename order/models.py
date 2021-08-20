from django.db import models
from account.models import User
from product.models import Product


# Create your models here.
class Wishlist(models.Model):
    wish_list_user = models.ForeignKey(User, on_delete=models.CASCADE)
    wish_list_product = models.ForeignKey(Product, on_delete=models.CASCADE)
    wish_list_status = models.BooleanField(default=False)

    def __str__(self):
        return self.wish_list_product.pro_name


class Cart(models.Model):
    cart_user = models.ForeignKey(User, on_delete=models.CASCADE)
    cart_product = models.ForeignKey(Product, on_delete=models.CASCADE)
    cart_quantity = models.IntegerField(default=1)
    cart_status = models.BooleanField(default=False)
    cart_color = models.CharField(max_length=50, null=True)
    cart_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.cart_product.pro_name

    @property
    def total_amount(self):
        return self.cart_product.total * self.cart_quantity
