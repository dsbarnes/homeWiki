from django.shortcuts import render, reverse
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Recipe

class RecipeListView(ListView):
    model = Recipe

class RecipeDetailView(DetailView):
    model = Recipe

class RecipeUpdateView(UpdateView):
    model = Recipe
    template_name_suffix = '_update_form'
    fields = ['name', 'time', 'ingredients', 'directions']
    def get_success_url(self):
        return reverse('recipe_list')

class RecipeCreateView(CreateView):
    model = Recipe
    template_name_suffix = '_create_form'
    fields = ['name', 'time', 'ingredients', 'directions']
    def get_success_url(self):
        return reverse('recipe_list')

class RecipeDeleteView(DeleteView):
    model = Recipe
    def get_success_url(self):
        return reverse('recipe_list')
