from django.urls import path
from .views import *

urlpatterns = [
    path(r'', members, name="members"),
    path('add_player/', add_player, name="add_player"),
    path('add_enemy/', add_enemy, name="add_enemy"),
    path(r'delete_player/(?P<id>\d+)', delete_player, name="delete_player"),
]