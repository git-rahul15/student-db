from django.urls import path
from . import views

urlpatterns = [
    path('complete-profile/', views.complete_profile, name='complete_profile'),
]