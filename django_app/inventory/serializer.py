from rest_framework import serializers
from inventory.models import Inventory


class InventorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Inventory
        field = (
            'name',
            'color',
            'size',
            'option',
            'quatity',
        )
