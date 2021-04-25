from django.shortcuts import render

# To render objects from DB to Template
from .models import Project

def home(request):
    projects = Project.objects.all()      # *****  grabs all the entries in the DB under Project and turns them to objects and stores them as List in projects variable
    return render(request, 'portfolio/home.html', {'projects': projects})  # pass an dict with DATA to Template