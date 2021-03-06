from django.urls import path
from .views import *

urlpatterns = [
    path(r'', combat_home, name="combat_home"),
    path('add_hero/', add_hero, name="add_hero"),
    path('start_combat/', start_combat, name="start_combat"),
    path(r'delete_hero_int/<int:pk>', delete_hero_int, name="delete_hero_int"),
    path(r'delete_all_from_combat/', delete_all_from_combat, name="delete_all_from_combat"),
    path(r'edit_hero/<int:pk>', edit_hero, name="edit_hero"),
    path(r'single_member/<int:pk>/', SingleCombatMember.as_view(), name="single_member"),
]