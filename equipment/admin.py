from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Weapon),
admin.site.register(Die),
admin.site.register(Skill)