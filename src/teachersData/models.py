from django.db import models

# Create your models here.
class Teacher(models.Model):
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