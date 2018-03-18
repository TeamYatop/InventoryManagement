from rest_framework import generics, mixins

from inventory.models import Inventory
from inventory.serializer import InventorySerializer


class InventoryAPI(mixins.ListModelMixin,
                   mixins.CreateModelMixin,
                   generics.GenericAPIView):
    queryset = Inventory.objects.all()
    serializer_class = InventorySerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, requset, *args, **kwargs):
        return self.create(requset, *args, **kwargs)
