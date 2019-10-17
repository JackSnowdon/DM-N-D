from django.urls import path
from .views import *

urlpatterns = [
    path(r'', members, name="members"),
    path('add_player/', add_player, name="add_player")
]