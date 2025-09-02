from django.db import models

# Create your models here.

class Managers(models.Model):
    
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    address = models.TextField()
    date_of_birth = models.DateField(null=True, blank=True)
    date_of_joining = models.DateField(null=True, blank=True, auto_created=True)
    photo = models.ImageField(upload_to='managers/', null=True, blank=True)
    is_active = models.BooleanField(default=True)