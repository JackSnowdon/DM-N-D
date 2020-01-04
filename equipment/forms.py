from django import forms
from .models import *

class AddWeapon(forms.ModelForm):

    class Meta:
        model = Weapon
        fields = '__all__'


class DieForm(forms.ModelForm):

    class Meta:
        model = Die
        fields = '__all__'
        
