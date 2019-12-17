from django.urls import path
from .views import *

urlpatterns = [
    path(r'', equipment_home, name="equipment_home"),
    path('add_weapon/', add_weapon, name="add_weapon"),
]