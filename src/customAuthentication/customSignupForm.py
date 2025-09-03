from django import forms
from .models import Profile  
from teachersData.models import Teacher# Import your Profile model
from managersData.models import Managers
from studentsData.models import Student
from django.shortcuts import redirect

class CustomSignupForm(forms.Form):

    CATEGORY_CHOICES = [
        ('student', 'Student'),
        ('teacher', 'Teacher'),
        ('manager', 'Manager'),
    ]
    category = forms.ChoiceField(choices=CATEGORY_CHOICES,initial="Teacher",widget=forms.RadioSelect, required=True)

    def signup(self,request, user):
        """This method is called after user creation"""
        category = self.cleaned_data.get('category')
        Profile.objects.create(user=user, category=category)
        user.save()
        if category == 'teacher':
            Teacher.objects.create(user=user, username=user.username, email=user.email)
        elif category == 'manager':
            Managers.objects.create(user=user, username=user.username, email=user.email)
        elif category == 'student':
            Student.objects.create(user=user, username=user.username, email=user.email)




    
