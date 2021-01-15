from django.urls import path 
from .views import GroceryListView, GroceryAddView, GroceryDeleteView, GroceryUpdateView

urlpatterns = [
    path('', GroceryListView.as_view(), name='grocery_list'),
    path('add/', GroceryAddView.as_view(), name='grocery_add'),
    path('update/', GroceryUpdateView.as_view(), name='grocery_update'),
    path('delete/', GroceryDeleteView.as_view(), name='grocery_delete'),
]
