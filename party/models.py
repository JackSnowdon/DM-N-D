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
    strengh = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(20)])
    dex = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(20)])
    intel = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(20)])
    wisdom = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(20)])
    con = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(20)])
    charisma = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(20)])
    
    
    def __str__(self):
        return self.name
        