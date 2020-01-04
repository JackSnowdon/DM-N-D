from django.urls import path
from .views import *

urlpatterns = [
    path(r'', equipment_home, name="equipment_home"),
    path('add_weapon/', add_weapon, name="add_weapon"),
    path('add_die/', add_die, name="add_die"),
    path(r'edit_weapon/<int:pk>', edit_weapon, name="edit_weapon"),
    path(r'delete_weapon/<int:pk>', delete_weapon, name="delete_weapon"),
]