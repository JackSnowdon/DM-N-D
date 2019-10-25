from django.db import models
from party.models import *

# Create your models here.
        
class CombatMember(models.Model):
    hero = models.OneToOneField(
        Base,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    initiative = models.IntegerField(max_length=2)
    current_hp = models.IntegerField(max_length=4)
    
    def __str__(self):
        return self.player.name
        