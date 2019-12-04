from django.db import models
from party.models import *

# Create your models here.


class Weapon(models.Model):
    name = models.CharField(max_length=50)
    die = models.IntegerField()
    

    def __str__(self):
        return '{0}'.format(self.name)