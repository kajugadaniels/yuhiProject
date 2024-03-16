from django.db import models
from account.models import User
from shortuuidfield import ShortUUIDField
from django.utils.html import mark_safe

def use_directory_path(instance, filename):
	return 'user_{0}/{1}'.format(instance.user.id, filename)

class Vendor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    vid = ShortUUIDField(unique=True, max_length=20)
    
    store_name = models.CharField(max_length=255, default="Store Name")
    manager_name = models.CharField(max_length=255, default="Enter manager name")
    phone_number = models.CharField(unique=True, max_length=20, default="078888888")
    email = models.EmailField(default="Enter email here")
    address = models.CharField(max_length=255, default="Address here")
    tin_number = models.CharField(max_length=20, default="1234567890")
    image = models.ImageField(upload_to=use_directory_path, default="vendor.jpg")
    
    class Meta:
        verbose_name_plural = "Vendors"

    def __str__(self):
        return self.store_name