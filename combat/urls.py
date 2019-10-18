from django.urls import path
from .views import *

urlpatterns = [
    path(r'', combat_home, name="combat_home"),
    path('add_hero/', add_hero, name="add_hero"),
    path('add_monster/', add_monster, name="add_monster"),
]