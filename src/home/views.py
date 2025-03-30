from django.shortcuts import render
from .models import visits
from django.contrib.auth.decorators import login_required



@login_required
def home_page(request, *args, **kwargs ):
    path = request.path
    
    visits.objects.create(path= path)
    queryset = visits.objects.all()
    total_visits = queryset.count()
    return render(request, "home.html", context={"visits":total_visits})

# Create your views here.
