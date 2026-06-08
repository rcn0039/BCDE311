from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required

from .models import Event
# Create your views here.

def index(request):
    return render(request, "index.html")

def search(request):
    return render(request, "search.html")

def project(request, id):
    return render(request, "project.html", {'project': {}})