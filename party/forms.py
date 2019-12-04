from django import forms

from .models import *

class PlayerForm(forms.ModelForm):

    class Meta:
        model = Base
        exclude = ['alignment', 'weapons']
        labels = {
            "max_hp": "Max HP",
            "dex": "Dexterity",
            "intel": "Intelligence",
            "con": "Constitution"
        }
        
class EnemyForm(forms.ModelForm):

    class Meta:
        model = Base
        exclude = ['alignment', 'weapons']
        labels = {
            "max_hp": "Max HP",
            "dex": "Dexterity",
            "intel": "Intelligence",
            "con": "Constitution"
        }