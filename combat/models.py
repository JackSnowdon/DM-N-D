from django.db import models
from party.models import *

# Create your models here.
        
class Player(models.Model):
    player = models.OneToOneField(
        Base,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    
    initiative = models.IntegerField(max_length=2)
    
    def __str__(self):
        return self.player.name
        
class Monster(models.Model):
    monster = models.OneToOneField(
        EnemyBase,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    
    initiative = models.IntegerField(max_length=2)
    
    def __str__(self):
        return self.monster.name