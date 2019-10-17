from django.urls import path
from .views import *

urlpatterns = [
    path(r'', combat_home, name="combat_home"),
]