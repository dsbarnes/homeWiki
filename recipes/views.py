from django.shortcuts import render, reverse
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Recipe

class RecipeListView(ListView):
    model = Recipe

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['ingredient_list'] = {}
        for recipe in context['object_list']:
            ingredients = [ingredient.strip() for ingredient in recipe.ingredients.split(',')]
            context['ingredient_list'][recipe.slug] = ingredients
            print(context)
        return context

class RecipeDetailView(DetailView):
    model = Recipe


class RecipeUpdateView(UpdateView):
    model = Recipe
    template_name_suffix = '_update_form'
    fields = ['name', 'time', 'ingredients', 'directions']

    def get_success_url(self):
        return reverse('recipe_liest')


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