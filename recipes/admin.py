from django.contrib import admin
from .models import Recipe

# Register your models here.
class RecipeAdmin(admin.ModelAdmin):
    fields = ['name', 'ingredients', 'directions', 'time', 'slug']
    prepopulated_fields = {'slug': ('name', )}

admin.site.register(Recipe, RecipeAdmin)