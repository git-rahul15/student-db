from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save


class Profile(models.Model):
     
     CATEGORY_CHOICES = [
        ('student', 'Student'),
        ('teacher', 'Teacher'),
        ('Manager', 'Manager'),
        ]
     user = models.OneToOneField(User, on_delete=models.CASCADE)
     category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)




