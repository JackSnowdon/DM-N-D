from django import forms

from .models import *

class AddToCombat(forms.ModelForm):

    class Meta:
        model = CombatMember
        fields = '__all__'
        labels = {
            "hero": "Combatant"
        }