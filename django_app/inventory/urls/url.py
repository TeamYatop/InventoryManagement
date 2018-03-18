from django.urls import path

from inventory import views

app_name = 'inventory'
urlpatterns = [
    path('', views.InventoryListView.as_view(), name='list'),
]
