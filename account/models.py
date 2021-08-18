from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    address = models.TextField(null=True)
    zip = models.BigIntegerField(null=True)
    phone = models.BigIntegerField(null=True)