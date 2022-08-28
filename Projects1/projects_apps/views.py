from django.shortcuts import render
from django.http import HttpResponse
from . import forms


# Create your views here.

def index(request):
    diction = {'sample_text': "Sample text"}
    return render(request, 'projects_apps/index.html')

def form(request):
    return render(request, 'projects_apps/form.html')
