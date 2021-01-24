from django.contrib import admin
from .models import Recipt, Grocery, GroceryListItem


class ReciptAdmin(admin.ModelAdmin):
    fields = ['name', 'reciept', 'slug']
    prepopulated_fields = {'slug': ('name', )}

class GroceryListItemAdmin(admin.ModelAdmin):
    fields = ['name']

class GroceryAdmin(admin.ModelAdmin):
    fields = ['name', 'quantity', 'cost', 'date', 'slug']
    prepopulated_fields = {'slug': ('name', )}


admin.site.register(Recipt, ReciptAdmin)
admin.site.register(Grocery, GroceryAdmin)
admin.site.register(GroceryListItem, GroceryListItemAdmin)