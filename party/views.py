from django.shortcuts import render, redirect, reverse
from .models import * 
from .forms import *

# Create your views here.

def members(request):
    players = Base.objects.order_by('name')
    return render(request, 'members.html', {"players": players})
    
def add_player(request):
    if request.method == "POST":
        player_form = PlayerForm(request.POST)
        if player_form.is_valid():
            player_form.save()
            return redirect('members')
    else:
        player_form = PlayerForm()
    return render(request, 'add_player.html', {'player_form': player_form})
    
def add_enemy(request):
    if request.method == "POST":
        enemy_form = EnemyForm(request.POST)
        if enemy_form.is_valid():
            form = enemy_form.save(commit=False)
            form.enemy = True
            form.save()
            return redirect('members')
    else:
        enemy_form = EnemyForm()
    return render(request, 'add_enemy.html', {'enemy_form': enemy_form})
    
def delete_player(request, id):
    instance = Base.objects.get(id=id)
    instance.delete()
    return redirect(reverse('members'))
    