from django.shortcuts import render, redirect, reverse
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
    
def delete_hero_combat(request, pk=id):
    print(pk)
    players = Base.objects.all()
    monsters = EnemyBase.objects.all()
    matches = list(chain(players, monsters))
    for m in matches:
        obj=m.id
        matches.remove()
    return redirect(reverse('combat_home'))
    