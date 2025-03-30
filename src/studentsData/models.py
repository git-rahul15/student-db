from django.db import models

# Create your models here.

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
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='students/')
    is_active = models.BooleanField(default=True)
    
