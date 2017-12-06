from rest_framework import serializers
from inventory.models import Task


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'

    def create(self, validated_data):
        if validated_data["action"] == "ADD":
            validated_data["inventory"].quantity += validated_data["value"]
        else:
            validated_data["inventory"].quantity -= validated_data["value"]
        validated_data["inventory"].save()
        return Task.objects.create(**validated_data)

    def validate(self, data):
        if data["action"] == "SUB":
            if data["value"] > data["inventory"].quantity:
                raise serializers.ValidationError("Value must be Smaller then quatities")
        return data
