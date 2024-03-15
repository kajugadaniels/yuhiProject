from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    is_vendor = models.BooleanField('Is vendor', default=False)
    is_customer = models.BooleanField('Is customer', default=False)