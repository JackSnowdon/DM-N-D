from django.db import models

# Create your models here.

Player = 'Player'
NPC = 'NPC'
    
alignment_choices = (
    (NPC, 'NPC'),
    (Player, 'Player'),
)

class Base(models.Model):
    name = models.CharField(max_length=100)
    alignment = models.CharField(max_length=32, choices=alignment_choices, default=Player)
    max_hp = models.IntegerField()
    
    
    def __str__(self):
        return self.name
        