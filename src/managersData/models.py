from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# Create your models here.



class Managers(models.Model):
    user = models.OneToOneField(User, primary_key=True, on_delete=models.CASCADE, default=None, related_name='manager')
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    address = models.TextField()
    date_of_birth = models.DateField(null=True, blank=True)
    date_of_joining = models.DateField(null=True, blank=True, auto_now_add=True)
    photo = models.ImageField(upload_to='managers/')
    is_active = models.BooleanField(default=True)