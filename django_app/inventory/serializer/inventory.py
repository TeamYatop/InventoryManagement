from rest_framework import serializers
from inventory.models import Inventory


class InventorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Inventory
        fields = (
            'name',
            'color',
            'size',
            'option',
            'quantity',
        )
        read_only_fields = (
            'quantity',
        )


class InventoryInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Inventory
        fields = (
            'name',
            'color',
            'size',
            'option',
        )
