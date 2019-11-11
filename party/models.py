from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator 

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
    max_hp = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5000)])
    strengh = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(30)])
    dex = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(30)])
    intel = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(30)])
    wisdom = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(30)])
    con = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(30)])
    charisma = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(30)])
    
    
    def __str__(self):
        return self.name
        