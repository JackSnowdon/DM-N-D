from django.shortcuts import render, redirect, reverse
from .models import * 
from .forms import *

# Create your views here.

def members(request):
    players = Player.objects.order_by('name')
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
    
def delete_player(request, id):
    instance = Player.objects.get(id=id)
    instance.delete()
    return redirect(reverse('members'))
    