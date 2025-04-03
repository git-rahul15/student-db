from django.db import models
from django.dispatch import receiver
from django.utils.text import slugify   
from django.db.models.signals import pre_save
import random
import string


def generate_unique_code(instance):
    base_name = slugify(instance.name)[:3].upper()  # Take first 3 characters of slugified name
    while True:
        random_part = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
        teacher_code = f"{base_name}{random_part}"
        if not Teacher.objects.filter(teacher_code=teacher_code).exists():
            return teacher_code

# Create your models here.
class Teacher(models.Model):
    teacher_id = models.AutoField(primary_key=True)
    teacher_code = models.CharField(max_length=50, unique=True, auto_created=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    address = models.TextField()
    subject_specialization = models.CharField(max_length=100, null=True, blank=True)
    hire_date = models.DateField(null=True, blank=True)
    years_of_experience = models.IntegerField(null=True, blank=True)
    photo = models.ImageField(upload_to='teachers/', null=True, blank=True)
    is_active = models.BooleanField(default=True)