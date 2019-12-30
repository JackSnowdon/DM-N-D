from django.shortcuts import render, redirect, reverse
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