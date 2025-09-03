from django import forms
from .models import Profile
from teachersData.models import Teacher
from managersData.models import Managers
from studentsData.models import Student

# Import SignupForm inside the class to avoid circular import
class CustomSignupForm:
    @staticmethod
    def get_form_class():
        from allauth.account.forms import SignupForm

        class _CustomSignupForm(SignupForm):
            CATEGORY_CHOICES = [
                ('student', 'Student'),
                ('teacher', 'Teacher'),
                ('manager', 'Manager'),
            ]
            category = forms.ChoiceField(choices=CATEGORY_CHOICES, initial="teacher", widget=forms.RadioSelect, required=True)

            def save(self, request):
                user = super().save(request)
                category = self.cleaned_data.get('category')
                Profile.objects.create(user=user, category=category)
                if category == 'teacher':
                    Teacher.objects.create(user=user, username=user.username, email=user.email)
                elif category == 'manager':
                    Managers.objects.create(user=user, username=user.username, email=user.email)
                elif category == 'student':
                    Student.objects.create(user=user, username=user.username, email=user.email)
                return user

        return _CustomSignupForm

# Create the actual form class
CustomSignupForm = CustomSignupForm.get_form_class()




    
