from django.urls import path
from .views import *

urlpatterns = [
    path(r'', members, name="members"),
    path('monsters/', monsters, name="monsters"),
    path('add_player/', add_player, name="add_player"),
    path('add_enemy/', add_enemy, name="add_enemy"),
    path(r'delete_player/<int:pk>', delete_player, name="delete_player"),
    path(r'delete_monster/<int:pk>', delete_monster, name="delete_monster"),
    path(r'edit_player/<int:pk>', edit_player, name="edit_player"),
    path(r'edit_monster/<int:pk>', edit_monster, name="edit_monster"),
]