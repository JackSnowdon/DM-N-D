from django.shortcuts import render
from .models import Weapon
from .forms import *

# Create your views here.

def equipment_home(request):
    weapons = Weapon.objects.order_by('name')
    return render(request, 'equip_home.html', {"weapons": weapons})

def add_weapon(request):
    if request.method == "POST":
        wepaon_form = AddWeapon(request.POST)
        if wepaon_form.is_valid():
            weapon_form.save()
            messages.error(request, 'Added {0}'.format(wepaon_form.name), extra_tags='alert boldest')
            return redirect('equipment_home')
    else:
        wepaon_form = AddWeapon()
    return render(request, 'add_weapon.html', {'wepaon_form': wepaon_form})