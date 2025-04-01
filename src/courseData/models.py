from django.db import models
from django.dispatch import receiver
from django.utils.text import slugify   
from django.db.models.signals import pre_save
import random
import string

# Create your models here.
def generate_unique_code(instance):
    base_name = slugify(instance.name)[:3].upper()  # Take first 3 characters of slugified name
    while True:
        random_part = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
        code = f"{base_name}{random_part}"
        if not Course.objects.filter(code=code).exists():
            return code

# Create your models here.
class Subject(models.Model):
    subject = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    
    
class Course(models.Model):
    name = models.CharField(max_length=100, default="Course Name")
    code = models.CharField(max_length=50, unique=True, auto_created=True)
    description = models.TextField(null=True, blank=True)
    date_added = models.DateField(auto_now_add=True)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    subjects = models.ManyToManyField(Subject)
    
@receiver(pre_save, sender=Course)
def set_unique_code(sender, instance, **kwargs):
    if not instance.code:
        instance.code = generate_unique_code(instance)
    