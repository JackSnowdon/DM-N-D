from django.db import models
from party.models import *
from django.core.validators import MaxValueValidator, MinValueValidator 


# Create your models here.
        
class CombatMember(models.Model):
    hero = models.OneToOneField(
        Base,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    initiative = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(30)])
    current_hp = models.PositiveIntegerField(validators=[MinValueValidator(0), MaxValueValidator(5000)])
    
    def __str__(self):
        return self.hero.name
        