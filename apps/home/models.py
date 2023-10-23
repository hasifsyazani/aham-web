from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class CustomerInfo(models.Model):
    first_name = models.CharField(max_length=50, blank=True, null=True)
    last_name = models.CharField(max_length=50, blank=True, null=True)
    email_address = models.CharField(max_length=100, blank=True, null=True)
    phone_no = models.CharField(max_length=30, blank=True, null=True)
    address = models.CharField(max_length=1000, blank=True, null=True)
    date_modified = models.DateTimeField(blank=True, null=True)
    
    def __str__(self):
        return str(self.first_name)
    

