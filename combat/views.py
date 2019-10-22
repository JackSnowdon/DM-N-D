from django.shortcuts import render, redirect, reverse, get_object_or_404
from itertools import chain
from .models import * 
from .forms import *
from party.models import * 

# Create your views here.



def combat_home(request):
    party = Player.objects.order_by('-initiative')
    enemy = Monster.objects.order_by('-initiative')
    matches = list(chain(party, enemy))
    return render(request, 'combat_home.html', {"party": party, "enemy": enemy, "matches": matches})
    
def add_hero(request):
    if request.method == "POST":
        hero_form = AddPlayerForm(request.POST)
        if hero_form.is_valid():
            hero_form.save()
            return redirect('combat_home')
    else:
        hero_form = AddPlayerForm()
    return render(request, 'add_hero.html', {'hero_form': hero_form})
    
def add_monster(request):
    if request.method == "POST":
        monster_form = AddMonsterForm(request.POST)
        if monster_form.is_valid():
            monster_form.save()
            return redirect('combat_home')
    else:
        monster_form = AddMonsterForm()
    return render(request, 'add_monster.html', {'monster_form': monster_form})
    
def delete_hero_int(request, pk=id):
    instance = Player.objects.get(player_id=pk)
    instance.delete()
    return redirect(reverse('combat_home'))
    
def delete_monster_int(request, pk=id):
    instance = Monster.objects.get(monster_id=pk)
    instance.delete()
    return redirect(reverse('combat_home'))
    
def edit_hero(request, pk):
    hero = get_object_or_404(Player, pk=pk)
    if request.method == "POST":
        hero_form = AddPlayerForm(request.POST, instance=hero)
        if hero_form.is_valid():
            hero_form.save()
            return redirect('combat_home')
    else:
        hero_form = AddPlayerForm(instance=hero)
    return render(request, 'edit_hero.html', {'hero_form': hero_form})
    
def edit_monster(request, pk):
    enemy = get_object_or_404(Monster, pk=pk)
    if request.method == "POST":
        monster_form = AddMonsterForm(request.POST, instance=enemy)
        if monster_form.is_valid():
            monster_form.save()
            return redirect('combat_home')
    else:
        monster_form = AddMonsterForm(instance=enemy)
    return render(request, 'edit_monster.html', {'monster_form': monster_form})
    