from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Profile
from teachersData.models import Teacher
from studentsData.models import Student
from managersData.models import Managers
from allauth.account.decorators import verified_email_required
from django.contrib.auth.models import User
from django import forms
from django.urls import reverse

def custom_signup(request):
    from allauth.account.forms import SignupForm

    class ExtendedSignupForm(SignupForm):
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

    if request.method == 'POST':
        form = ExtendedSignupForm(request.POST)
        if form.is_valid():
            user = form.save(request)
            messages.success(request, 'Account created successfully!')
            return redirect('account_email_verification_sent')
    else:
        form = ExtendedSignupForm()

    login_url = reverse('account_login')

    return render(request, 'account/signup.html', {'form': form, 'login_url': login_url})

@login_required
@verified_email_required
def complete_profile(request):
    profile = Profile.objects.get(user=request.user)
    category = profile.category

    if category == 'teacher':
        model_class = Teacher
        instance = Teacher.objects.filter(user=request.user).first()
    elif category == 'student':
        model_class = Student
        instance = Student.objects.filter(username=request.user.email).first()
    elif category == 'manager':
        model_class = Managers
        instance = Managers.objects.filter(email=request.user.email).first()

    if request.method == 'POST':
        # Update User fields
        request.user.first_name = request.POST.get('first_name', request.user.first_name)
        request.user.last_name = request.POST.get('last_name', request.user.last_name)
        request.user.save()

        # Update category-specific fields
        if not instance:
            instance = model_class()
            if category == 'teacher':
                instance.user = request.user
            elif category == 'student':
                instance.username = request.user.email
                instance.email = request.user.email
            elif category == 'manager':
                instance.email = request.user.email
        instance.user = request.user 
        instance.first_name = request.POST.get('first_name', getattr(instance, 'first_name', ''))
        instance.last_name = request.POST.get('last_name', getattr(instance, 'last_name', ''))
        instance.email = request.user.email
        instance.phone = request.POST.get('phone', getattr(instance, 'phone', ''))
        instance.address = request.POST.get('address', getattr(instance, 'address', ''))

        if category == 'teacher':
            instance.city = request.POST.get('city', getattr(instance, 'city', ''))
            instance.state = request.POST.get('state', getattr(instance, 'state', ''))
            instance.subject_specialization = request.POST.get('subject_specialization', getattr(instance, 'subject_specialization', ''))
            instance.hire_date = request.POST.get('hire_date', getattr(instance, 'hire_date', None))
            instance.years_of_experience = request.POST.get('years_of_experience', getattr(instance, 'years_of_experience', 0))
        elif category == 'student':
            instance.age = request.POST.get('age', getattr(instance, 'age', None))
            instance.date_of_birth = request.POST.get('date_of_birth', getattr(instance, 'date_of_birth', None))
            instance.date_of_admission = request.POST.get('date_of_admission', getattr(instance, 'date_of_admission', None))
        elif category == 'manager':
            instance.date_of_birth = request.POST.get('date_of_birth', getattr(instance, 'date_of_birth', None))
            instance.date_of_joining = request.POST.get('date_of_joining', getattr(instance, 'date_of_joining', None))

        if 'photo' in request.FILES:
            instance.photo = request.FILES['photo']

        instance.save()
        return redirect('/')

    context = {
        'profile': profile,
        'instance': instance,
        'category': category,
    }
    return render(request, 'profile/complete_profile.html', context)

