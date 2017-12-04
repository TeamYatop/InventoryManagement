from django.conf.urls import url
from inventory.api import InventoryAPI

urlpatterns = [
    url(r'^inventory/$', InventoryAPI.as_view(), name='inventory')
]