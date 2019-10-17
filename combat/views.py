from django.shortcuts import render, redirect
from .models import * 
from .forms import *

# Create your views here.

def combat_home(request):
    return render(request, 'combat_home.html')
    