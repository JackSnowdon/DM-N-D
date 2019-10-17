from django.urls import path
from .views import *

urlpatterns = [
    path(r'', members, name="members"),
]