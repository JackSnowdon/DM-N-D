from django.shortcuts import render, redirect
from .models import * 
from .forms import *

# Create your views here.

def combat_home(request):
    enemies = Enemy.objects.order_by('name')
    return render(request, 'combat_home.html', {"enemies": enemies})
    
def add_enemy(request):
    if request.method == "POST":
        enemy_form = EnemyForm(request.POST)
        if enemy_form.is_valid():
            enemy_form.save()
            return redirect('combat_home')
    else:
        enemy_form = EnemyForm()
    return render(request, 'add_enemy.html', {'enemy_form': enemy_form})