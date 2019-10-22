from django.urls import path
from .views import *

urlpatterns = [
    path(r'', combat_home, name="combat_home"),
    path('add_hero/', add_hero, name="add_hero"),
    path('add_monster/', add_monster, name="add_monster"),
    path(r'delete_hero_int/<int:pk>', delete_hero_int, name="delete_hero_int"),
    path(r'delete_monster_int/<int:pk>', delete_monster_int, name="delete_monster_int"),
    path(r'edit_hero/<int:pk>', edit_hero, name="edit_hero"),
    path(r'edit_monster/<int:pk>', edit_monster, name="edit_monster"),
]