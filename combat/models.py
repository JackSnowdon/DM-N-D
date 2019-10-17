from django.db import models

# Create your models here.

class Enemy(models.Model):
    name = models.CharField(max_length=100)
    hp = models.IntegerField()
    initiative = models.IntegerField(max_length=2)
    
    def __str__(self):
        return self.name