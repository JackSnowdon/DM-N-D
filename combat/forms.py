from django import forms

from .models import *

class AddPlayerForm(forms.ModelForm):

    class Meta:
        model = Player
        fields = '__all__'
        
class AddMonsterForm(forms.ModelForm):

    class Meta:
        model = Monster
        exclude = '__all__'