from django.db import models
from teachersData.models import Teacher
from courseData.models import Course, Subject 
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField



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
 
    
class School(models.Model):
    name = models.CharField(max_length=100)
    address = models.TextField(null=True, blank=True)
    phone = models.CharField(max_length=20, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    principal = models.CharField(max_length=100, null=True, blank=True)
    established_date = models.DateField(null=True, blank=True)
    website = models.URLField(null=True, blank=True)

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, default=None)
    username = models.CharField(max_length=100, unique=True, null=True, blank=True)
    id = models.AutoField(primary_key=True, editable=False, auto_created=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    age = models.IntegerField()
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
    
