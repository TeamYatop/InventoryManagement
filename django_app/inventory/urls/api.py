from django.urls import path

from inventory import api

app_name = 'inventory-api'
urlpatterns = [
    path('inventory/', api.InventoryAPI.as_view(), name='inventory'),
    path('task/', api.TaskAPI.as_view(), name='task'),
]
