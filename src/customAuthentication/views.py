from django.shortcuts import render, redirect
from teachersData.models import Teacher
from studentsData.models import Student
from allauth.account.decorators import verified_email_required

