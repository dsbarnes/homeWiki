from django.urls import path 
from .views import GroceryListView, GroceryCreateView, GroceryDeleteView, GroceryUpdateView

urlpatterns = [
    path('', GroceryListView.as_view(), name='grocery_list'),
    path('create/', GroceryCreateView.as_view(), name='grocery_create'),
    path('update/', GroceryUpdateView.as_view(), name='grocery_update'),
    path('delete/', GroceryDeleteView.as_view(), name='grocery_delete'),
]
