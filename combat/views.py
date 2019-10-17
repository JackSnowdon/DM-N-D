from django.shortcuts import render

# Create your views here.

def combat_home(request):
    return render(request, 'combat_home.html')