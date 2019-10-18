from django.db import models

# Create your models here.

class Base(models.Model):
    name = models.CharField(max_length=100)
    hp = models.IntegerField()
    
    
    def __str__(self):
        return self.name
        
class EnemyBase(models.Model):
    name = models.CharField(max_length=100)
    hp = models.IntegerField()
    
    
    def __str__(self):
        return self.name