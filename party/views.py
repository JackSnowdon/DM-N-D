from django.shortcuts import render, redirect, reverse
from .models import * 
from .forms import *

# Create your views here.

def members(request):
    get_players = Base.objects.order_by('name')
    players = get_players.filter(alignment='Player')
    return render(request, 'members.html', {"players": players})
    
def add_player(request):
    if request.method == "POST":
        player_form = PlayerForm(request.POST)
        if player_form.is_valid():
            player = player_form.save(commit=False)
            player.alignment = 'Player'
            player.save()
            return redirect('members')
    else:
        player_form = PlayerForm()
    return render(request, 'add_player.html', {'player_form': player_form})

def monsters(request):
    get_monsters = Base.objects.order_by('name')
    monsters = get_monsters.filter(alignment='NPC')
    return render(request, 'monsters.html', {"monsters": monsters})
    
def add_enemy(request):
    if request.method == "POST":
        enemy_form = EnemyForm(request.POST)
        if enemy_form.is_valid():
            enemy = enemy_form.save(commit=False)
            enemy.alignment = 'NPC'
            enemy.save()
            return redirect('monsters')
    else:
        enemy_form = EnemyForm()
    return render(request, 'add_enemy.html', {'enemy_form': enemy_form})
    
def delete_player(request, pk=id):
    instance = Base.objects.get(id=pk)
    instance.delete()
    return redirect(reverse('members'))
    
def delete_monster(request, pk=id):
    instance = Base.objects.get(id=pk)
    instance.delete()
    return redirect(reverse('monsters'))
    