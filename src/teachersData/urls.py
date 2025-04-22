
from django.urls import path
from . import views

urlpatterns = [
    path('complete-profile/', views.complete_teacher_profile, name='complete_teacher_profile'),
]
