from django.db import models

SIZE_CODE = (
    ('XXS', 'DoubleExtraSmall'),
    ('XS', 'ExtraSmall'),
    ('S', 'Small'),
    ('M', 'Medium'),
    ('L', 'Large'),
    ('XL', 'ExtraLarge'),
    ('XXL', 'DoubleExtraLarge'),
)
OPTION_CODE = (
    ('NA', 'none'),
)


class Inventory(models.Model):
    class Meta:
        unique_together = (("name", "color", "size", "option"),)

    name = models.CharField(max_length=60)
    color = models.CharField(max_length=40)
    size = models.CharField(max_length=3, choices=SIZE_CODE)
    option = models.CharField(max_length=4, choices=OPTION_CODE)
    quantity = models.PositiveIntegerField(default=0)

    def __str__(self):
        return '({},{},{},{})'.format(
            self.name,
            self.color,
            self.size,
            self.option,
        )

    @classmethod
    def get_by_name_color_pairs(cls):
        queryset = Inventory.objects.all()

        inventory_in_name_color_pair = dict()
        for inventory in queryset:
            name_color = "{}:{}".format(inventory.name, inventory.color)
            if name_color not in inventory_in_name_color_pair:
                inventory_in_name_color_pair[name_color] = dict()
            inventory_in_name_color_pair[name_color][inventory.size] = inventory.quantity

        return inventory_in_name_color_pair
