from django.urls import path

from . import api

urlpatterns = [
    path('inventory/', api.InventoryAPI.as_view(), name='inventory'),
    path('task/', api.TaskAPI.as_view(), name='task'),
]
