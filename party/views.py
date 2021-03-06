from django.shortcuts import render, redirect, reverse, get_object_or_404
from .models import * 
from .forms import *
from django.contrib import messages

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
            player.owner = request.user.profile
            player.save()
            messages.error(request, 'Added {0}'.format(player.name), extra_tags='alert boldest')
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
            enemy.owner = request.user.profile
            enemy.save()
            messages.error(request, 'Added {0}'.format(enemy.name), extra_tags='alert boldest')
            return redirect('monsters')
    else:
        enemy_form = EnemyForm()
    return render(request, 'add_enemy.html', {'enemy_form': enemy_form})
    
def delete_player(request, pk=id):
    instance = Base.objects.get(id=pk)
    if request.user.profile == instance.owner:
        instance.delete()
        messages.error(request, 'Deleted {0}'.format(instance.name), extra_tags='alert boldest')
    else: 
        messages.error(request, 'Only {0} can delete this Hero!'.format(instance.owner), extra_tags='alert boldest')
    return redirect(reverse('members'))
    
def delete_monster(request, pk=id):
    instance = Base.objects.get(id=pk)
    if request.user.profile == instance.owner:
        instance.delete()
        messages.error(request, 'Deleted {0}'.format(instance.name), extra_tags='alert boldest')
    else: 
        messages.error(request, 'Only {0} can delete this Hero!'.format(instance.owner), extra_tags='alert boldest')
    return redirect(reverse('monsters'))

def edit_player(request, pk):
    hero = get_object_or_404(Base, pk=pk)
    if request.user.profile == hero.owner:
        if request.method == "POST":
            hero_form = PlayerForm(request.POST, instance=hero)
            if hero_form.is_valid():
                player = hero_form.save(commit=False)
                player.alignment = 'Player'
                player.save()
                hero_form.save_m2m()
                messages.warning(request, 'Edited {0}'.format(player.name), extra_tags='alert boldest')
                return redirect('members')
        else:
            hero_form = PlayerForm(instance=hero)
    else:
        messages.error(request, 'Only {0} can edit {1}!'.format(hero.owner, hero.name), extra_tags='alert boldest')
        return redirect(reverse('members'))
    
    return render(request, 'edit_player.html', {'hero_form': hero_form, "hero": hero})
    
def edit_monster(request, pk):
    monster = get_object_or_404(Base, pk=pk)
    if request.user.profile == monster.owner:
        if request.method == "POST":
            monster_form = EnemyForm(request.POST, instance=monster)
            if monster_form.is_valid():
                monster = monster_form.save(commit=False)
                monster.alignment = 'NPC'
                monster.save()
                monster_form.save_m2m()
                messages.warning(request, 'Edited {0}'.format(monster.name), extra_tags='alert boldest')
                return redirect('monsters')
        else:
            monster_form = EnemyForm(instance=monster)
    else:
        messages.error(request, 'Only {0} can edit {1}!'.format(monster.owner, monster.name), extra_tags='alert boldest')
        return redirect(reverse('monsters'))
    return render(request, 'edit_monster.html', {'monster_form': monster_form, "monster": monster})