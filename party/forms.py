from django import forms

from .models import *

class PlayerForm(forms.ModelForm):

    class Meta:
        model = Base
        exclude = ['alignment']
        labels = {
            "max_hp": "Max HP"
        }
        
class EnemyForm(forms.ModelForm):

    class Meta:
        model = Base
        exclude = ['alignment']
        labels = {
            "max_hp": "Max HP"
        }