from django.shortcuts import render, redirect, reverse, get_object_or_404
from itertools import chain
from .models import *
from .forms import *
from party.models import * 

# Create your views here.

def combat_home(request):
    party = CombatMember.objects.order_by('-initiative')
    return render(request, 'combat_home.html', {"party": party})
    
def add_hero(request):
    if request.method == "POST":
        hero_form = AddToCombat(request.POST)
        if hero_form.is_valid():
            hero_form.save()
            return redirect('combat_home')
    else:
        hero_form = AddToCombat()
    return render(request, 'add_hero.html', {'hero_form': hero_form})
    
    
def delete_hero_int(request, pk=id):
    instance = CombatMember.objects.get(hero_id=pk)
    instance.delete()
    return redirect(reverse('combat_home'))
    
def delete_all_from_combat(request):
    CombatMember.objects.all().delete()
    return redirect(reverse('combat_home'))
    
def edit_hero(request, pk):
    hero = get_object_or_404(CombatMember, pk=pk)
    if request.method == "POST":
        hero_form = EditCombat(request.POST, instance=hero)
        if hero_form.is_valid():
            form = hero_form.save(commit=False)
            form.alignment = hero.hero
            form.save()
            return redirect('combat_home')
    else:
        hero_form = EditCombat(instance=hero)
    return render(request, 'edit_hero.html', {'hero_form': hero_form, 'hero':hero})
    
    
    