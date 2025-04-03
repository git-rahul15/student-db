from django import forms
from .models import Profile  # Import your Profile model

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
