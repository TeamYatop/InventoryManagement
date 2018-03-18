from django.views.generic import TemplateView

from inventory.models import Inventory


class InventoryListView(TemplateView):
    template_name = 'inventory/inventory_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['inventory_list'] = Inventory.objects.all()
        return context
