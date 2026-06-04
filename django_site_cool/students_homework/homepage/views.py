from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request, 'homepage/index.html')

def about(request):
    return render(request, 'homepage/about.html')

def contacts(request):
    return render(request, 'homepage/contacts.html')

def tasks(request):
    return render(request, 'homepage/tasks.html')