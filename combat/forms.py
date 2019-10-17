from django import forms

from .models import *

class EnemyForm(forms.ModelForm):

    class Meta:
        model = Enemy
        fields = '__all__'