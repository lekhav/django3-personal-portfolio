from django.contrib import admin

from .models import Project
# Specify what models to show up for the Admin
admin.site.register(Project)

