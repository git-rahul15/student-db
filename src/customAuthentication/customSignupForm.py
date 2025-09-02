from django import forms
from .models import Profile  
from teachersData.models import Teacher# Import your Profile model
from managersData.models import Managers
from studentsData.models import Student

class CustomSignupForm(forms.Form):
    CATEGORY_CHOICES = [
        ('student', 'Student'),
        ('teacher', 'Teacher'),
        ('manager', 'Manager'),
    ]
    category = forms.ChoiceField(choices=CATEGORY_CHOICES,initial="Teacher",widget=forms.RadioSelect, required=True)

    def signup(self, request, user):
        """This method is called after user creation"""
        category = self.cleaned_data.get('category')
        Profile.objects.create(user=user, category=category)
        user.save()
        if category == 'teacher':
            teacher = Teacher.objects.create(user=user, username=user.username,email=user.email)
            teacher.save()
        if category == 'manager':
            manager = Managers.objects.create(user=user, username=user.username,email=user.email)
            manager.save()
        if category == 'student':
            student = Student.objects.create(email=user.email)
            student.save()
        



    
