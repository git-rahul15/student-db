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
    
class Grade(models.Model):
    ...

class Parent(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    address = models.TextField()
    occupation = models.CharField(max_length=100, null=True, blank=True)
    relationship_to_student = models.CharField(max_length=50, null=True, blank=True)
    
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
    
class School(models.Model):
    name = models.CharField(max_length=100)
    address = models.TextField(null=True, blank=True)
    phone = models.CharField(max_length=20, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    principal = models.CharField(max_length=100, null=True, blank=True)
    established_date = models.DateField(null=True, blank=True)
    website = models.URLField(null=True, blank=True)

class Student(models.Model):
    id = models.AutoField(primary_key=True, editable=False, auto_created=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    age = models.IntegerField
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    address = models.TextField()
    date_of_birth = models.DateField()
    date_of_admission = models.DateField()
    subjects = models.ManyToManyField(Subject)
    courses = models.ManyToManyField(Course)
    grades = models.ManyToManyField(Grade)
    parents = models.ManyToManyField(Parent)
    teachers = models.ManyToManyField(Teacher)
    school = models.ForeignKey(School, on_delete=models.CASCADE, null=True, blank=True)
    photo = models.ImageField(upload_to='students/')
    is_active = models.BooleanField(default=True)
    
