from django.contrib import admin

# Register your models here.

# add two lines as below, and the Project table(model) will appear in the admin page

from .models import Project

admin.site.register(Project)
