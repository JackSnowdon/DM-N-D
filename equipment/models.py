from django.db import models
from party.models import *

# Create your models here.

D4 = 'D4'
D6 = 'D6'
D8 = 'D8'
D10 = 'D10'
D12 = 'D12'
D20 = 'D20'

DIE_CHOICES = (
    (D4, '4'),
    (D6, '6'),
    (D8, '8'),
    (D10, '10'),
    (D12, '12'),
    (D20, '20'),
)

Rogue = 'Rogue'

CLASS_CHOICES = (
    (Rogue, 'Rogue'),
)

class Die(models.Model):
    die = models.CharField(max_length=20, choices=DIE_CHOICES, default=D4)
    number_of_die = models.IntegerField()

    def __str__(self):
        return '{1}{0}'.format(self.die, self.number_of_die)



class Weapon(models.Model):
    name = models.CharField(max_length=50)
    die = models.ManyToManyField(Die)

    def __str__(self):
        return '{0}'.format(self.name)

    
class Skill(models.Model):
    name = models.CharField(max_length=50)
    die = models.ManyToManyField(Die)
    classpick = models.CharField(max_length=20, choices=CLASS_CHOICES, default=Rogue)

    def __str__(self):
        return '{0}'.format(self.name)