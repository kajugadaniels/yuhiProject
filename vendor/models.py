import shortuuid
from django.db import models
from account.models import User

class Vendor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    vid = models.CharField(max_length=30, unique=True, editable=False, default=f'vendor_{shortuuid.ShortUUID().random(length=10)}')
    store_name = models.CharField(max_length=255)
    manager_name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField()
    address = models.CharField(max_length=255)
    tin_number = models.CharField(max_length=20)
    image = models.ImageField(upload_to='vendor_images/')

    def __str__(self):
        return self.store_name