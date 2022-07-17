from django.shortcuts import render
from .models import Project

def home(request):
    projects = Project.objects.all()
    # grab everything in DB and turn them into python objects
    return render(request, 'portfolio/home.html', {'projects': projects})