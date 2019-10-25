from django.urls import path
from .views import *

urlpatterns = [
    path(r'', combat_home, name="combat_home"),
    path('add_hero/', add_hero, name="add_hero"),
    path(r'delete_hero_int/<int:pk>', delete_hero_int, name="delete_hero_int"),
    path(r'edit_hero/<int:pk>', edit_hero, name="edit_hero"),
]