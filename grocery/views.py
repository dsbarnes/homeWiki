from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Grocery

# Create your views here.
class GroceryListView(LoginRequiredMixin, ListView):
    model = Grocery
    login_url = 'login'

class GroceryDetailView(LoginRequiredMixin, DetailView):
    model = Grocery

class GroceryCreateView(LoginRequiredMixin, CreateView):
    model = Grocery
    template_name_suffix = '_create_form'
    def get_success_url(self):
        return reverse('grocery_list')

class GroceryUpdateView(LoginRequiredMixin, UpdateView):
    model = Grocery
    template_name_suffix = '_update_form'
    def get_success_url(self):
        return reverse('grocery_list')

class GroceryDeleteView(LoginRequiredMixin, DeleteView):
    model = Grocery
    def get_success_url(self):
        return reverse('grocery_list') 