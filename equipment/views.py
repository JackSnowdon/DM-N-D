from django.shortcuts import render
from .models import Weapon

# Create your views here.

def equipment_home(request):
    weapons = Weapon.objects.order_by('name')
    return render(request, 'equip_home.html', {"weapons": weapons})
