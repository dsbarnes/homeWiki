from django.urls import path
from .views import RecipeListView, RecipeCreateView, RecipeUpdateView, RecipeDeleteView, RecipeDetailView

urlpatterns = [
    path('', RecipeListView.as_view(), name='recipe_list'),
    path('recipe-detail/<slug:slug>/', RecipeDetailView.as_view(), name='recipe_detail'),
    path('recipe-create/', RecipeCreateView.as_view(), name='recipe_add'),
    path('recipe-update/<slug:slug>/', RecipeUpdateView.as_view(), name='recipe_update'),
    path('recipe-delete/<slug:slug>/', RecipeDeleteView.as_view(), name='recipe_delete'),
]
