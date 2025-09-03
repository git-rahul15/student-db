from django.shortcuts import render
from django.shortcuts import render, redirect
from .models import Teacher
from django.contrib.auth.decorators import login_required
from allauth.account.decorators import verified_email_required


