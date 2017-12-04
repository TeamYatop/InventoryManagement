from rest_framework import generics
from inventory.models import Inventory
from inventory.serializer import InventorySerializer


class InventoryAPI(generics.GenericAPIView):
    queryset = Inventory.objects.all()
    serializer_class = InventorySerializer
