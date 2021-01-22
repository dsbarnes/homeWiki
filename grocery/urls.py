from django.urls import path 
from .views import GroceryListView, GroceryCreateView, GroceryDeleteView, GroceryUpdateView, GroceryDetailView

urlpatterns = [
    path('', GroceryListView.as_view(), name='grocery_list'),
    path('create/', GroceryCreateView.as_view(), name='grocery_create'),
    path('detail/<slug:slug>', GroceryDetailView.as_view(), name='grocery_detail'),
    path('update/<slug:slug>', GroceryUpdateView.as_view(), name='grocery_update'),
    path('delete/<slug:slug>', GroceryDeleteView.as_view(), name='grocery_delete'),
]
