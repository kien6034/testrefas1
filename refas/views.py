from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import *

def home(request):
    archives = Archive.objects.all()
    context = {
        'archives': archives
    }
    return render(request, "refas/home.html", context = context)