from django.shortcuts import render
from django.shortcuts import render, redirect
from .models import Teacher
from django.contrib.auth.decorators import login_required

@login_required
def complete_teacher_profile(request):

    teacher = Teacher.objects.get(user=request.user)

    if request.method == 'POST':
        ...
    else:
        ...

    return render(request, 'teachers/complete_profile.html')
