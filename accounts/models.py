from django.db import models

# Create your models here.

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


"""
Upon User creation, Profile model is added and connected to a single user

"""

Adventurer = 'Adventurer'
DM = 'DM'

DMA_CHOICES = (
    (Adventurer, 'Adventurer'),
    (DM, 'DM')
)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    player_type = models.CharField(max_length=20, choices=DMA_CHOICES, default=Adventurer)
    
    def __str__(self):
        return "{0}".format(self.user)


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
