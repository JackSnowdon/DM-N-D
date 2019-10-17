from django.db import models
from party.models import *

# Create your models here.

class Enemy(models.Model):
    name = models.CharField(max_length=100)
    hp = models.IntegerField()
    initiative = models.IntegerField(max_length=2)
    
    def __str__(self):
        return self.name
        
class Member(models.Model):
    player = models.OneToOneField(
        Player,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    
    initiative = models.IntegerField(max_length=2)
    
    def __str__(self):
        return self.player.name