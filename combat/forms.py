from django import forms

from .models import *

class AddToCombat(forms.ModelForm):

    class Meta:
        model = CombatMember
        fields = '__all__'
        labels = {
            "hero": "Combatant",
            "current_hp": "Current HP"
        }
        
class EditCombat(forms.ModelForm):

    class Meta:
        model = CombatMember
        exclude = ['hero']
        labels = {
            "current_hp": "Current HP"
        }