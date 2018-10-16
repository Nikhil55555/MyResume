from django.shortcuts import render
from .models import Project

# Create your views here.
def nick(request):
    return render(request,'nick.html')

def home(request):
    projects=Project.objects
    return render(request,'home.html',{'projects':projects})
