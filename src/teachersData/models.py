from django.db import models
from django.dispatch import receiver
from django.utils.text import slugify   
from django.db.models.signals import pre_save
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator
import random
import string


def generate_unique_code(instance):
    base_name = slugify(instance.username)[:3].upper()  # Take first 3 characters of slugified name
    while True:
        random_part = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
        teacher_code = f"{base_name}{random_part}"
        if not Teacher.objects.filter(teacher_code=teacher_code).exists():
            return teacher_code

# Create your models here.
class Teacher(models.Model):
    user = models.OneToOneField(User, primary_key=True, on_delete=models.CASCADE, default=None)
    username = models.CharField(max_length=100, unique=True, null=True, blank=True)
    teacher_code = models.CharField(max_length=50, unique=True, auto_created=True, editable=False)
    first_name = models.CharField(max_length=100, null=True, blank=True)
    last_name = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField(blank=True, unique=True)
    phone = models.CharField(max_length=20, null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    city = models.CharField(max_length=100, null=True, blank=True)
    state = models.CharField(max_length=100, null=True, blank=True)
    subject_specialization = models.CharField(max_length=100, null=True, blank=True)
    hire_date = models.DateField(null=True, blank=True)
    years_of_experience = models.IntegerField(
        validators=[MinValueValidator(0)]
    )
    photo = models.ImageField(upload_to='teachers/', null=True, blank=True)
    is_active = models.BooleanField(default=True)


@receiver(pre_save, sender=Teacher)
def set_unique_code(sender, instance, **kwargs):
    if not instance.teacher_code:
        instance.teacher_code = generate_unique_code(instance)