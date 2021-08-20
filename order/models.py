from django.db import models
from account.models import User
from product.models import Product


# Create your models here.
class Wishlist(models.Model):
    wish_list_user = models.ForeignKey(User, on_delete=models.CASCADE)
    wish_list_product = models.ForeignKey(Product, on_delete=models.CASCADE)
    wish_list_status = models.BooleanField(default=False)
