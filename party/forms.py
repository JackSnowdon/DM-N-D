from django import forms

from .models import *

class PlayerForm(forms.ModelForm):

    class Meta:
        model = Base
        exclude = ['enemy']
        
class EnemyForm(forms.ModelForm):

    class Meta:
        model = Base
        exclude = ['enemy']