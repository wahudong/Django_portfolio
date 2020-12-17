from django.shortcuts import render
from .models import Project

# Create your views here.
def home(request):
  """
  docstring
  """
  projects= Project.objects.all()
  return render(request, 'portfolio/home.html', {'projects':projects})
