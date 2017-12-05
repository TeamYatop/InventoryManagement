from django.db import models
from inventory.models import inventory

ACTION_CODE = (
    ('ADD', 'task inventory add'),
    ('SUB', 'task inventory sub'),
)


class Task(models.Model):
    inventory = models.ForeignKey(inventory.Inventory)
    date = models.DateField(auto_now_add=True)
    action = models.CharField(max_length=4, choices=ACTION_CODE)
    value = models.PositiveIntegerField()

# class Task(models.Model):
#     date = models.DateField()
#     name = models.CharField(max_length=60)
#     color = models.CharField(max_length=40)
#     size = models.CharField(max_length=3, choices=SIZE_CODE)
#     option = models.CharField(max_length=4, choices=OPTION_CODE)
#     quantity = models.PositiveIntegerField(default=0)
