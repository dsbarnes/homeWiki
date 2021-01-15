from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Grocery

# Create your views here.
class GroceryListView(ListView):
    model = Grocery

class GroceryAddView(CreateView):
    model = Grocery

class GroceryUpdateView(UpdateView):
    model = Grocery

class GroceryDeleteView(DeleteView):
    model = Grocery