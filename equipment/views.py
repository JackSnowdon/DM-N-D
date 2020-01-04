from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from .models import Weapon
from .forms import *

# Create your views here.

def equipment_home(request):
    weapons = Weapon.objects.order_by('name')
    return render(request, 'equip_home.html', {"weapons": weapons})

def add_weapon(request):
    if request.method == "POST":
        weapon_form = AddWeapon(request.POST)
        if weapon_form.is_valid():

            
            """ 
            Below messages not passing
            messages.error(request, 'Added {0}'.format(weapon_form.name), extra_tags='alert boldest')
            """


            weapon_form.save()
            return redirect(reverse('equipment_home'))
    else:
        weapon_form = AddWeapon()
    return render(request, 'add_weapon.html', {'weapon_form': weapon_form})


def edit_weapon(request, pk):
    current_weapon = get_object_or_404(Weapon, pk=pk)
    if request.method == "POST":
        weapon_form = AddWeapon(request.POST, instance=current_weapon)
        if weapon_form.is_valid():
            weapon_form.save()
            """
            MEssages also not working, no name!?
            messages.warning(request, 'Edited {0}'.format(weapon_form.name), extra_tags='alert boldest')
            """
            return redirect('equipment_home')

    else:
        weapon_form = AddWeapon(instance=current_weapon)
    return render(request, 'edit_weapon.html', {'weapon_form': weapon_form, 'current_weapon': current_weapon})


def delete_weapon(request, pk):
    instance = Weapon.objects.get(id=pk)
    messages.warning(request, 'Deleted {0}'.format(instance.name), extra_tags='alert boldest')
    instance.delete()
    return redirect(reverse('equipment_home'))


def add_die(request):
    if request.method == "POST":
        die_form = DieForm(request.POST)
        if die_form.is_valid():

            #print(die_form)
            #die_value = request.POST.number_of_die + request.POST.die
            #print(die_value)

            
            
            
            # messages.error(request, 'Added {0}{1}'.format(die_form.number_of_die, die_form.die), extra_tags='alert boldest')
            


            die_form.save()
            return redirect(reverse('add_weapon'))
    else:
        die_form = DieForm()
    return render(request, 'add_die.html', {'die_form': die_form})