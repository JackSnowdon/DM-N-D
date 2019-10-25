from django import forms

from .models import *

class PlayerForm(forms.ModelForm):

    class Meta:
        model = Base
        exclude = ['alignment']
        
class EnemyForm(forms.ModelForm):

    class Meta:
        model = Base
        exclude = ['alignment']