from django.urls import path
from .views import *

urlpatterns = [
    path(r'', equipment_home, name="equipment_home"),
]