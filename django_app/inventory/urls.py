from django.conf.urls import url
from inventory import api

urlpatterns = [
    url(r'^inventory/$', api.InventoryAPI.as_view(), name='inventory')
]
