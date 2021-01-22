from django.contrib import admin
from .models import Recipt, Grocery


class ReciptAdmin(admin.ModelAdmin):
    fields = ['name', 'reciept', 'slug']
    prepopulated_fields = {'slug': ('name', )}

class GroceryAdmin(admin.ModelAdmin):
    fields = ['name', 'quantity', 'cost', 'date', 'slug']
    prepopulated_fields = {'slug': ('name', )}


admin.site.register(Recipt, ReciptAdmin)
admin.site.register(Grocery, GroceryAdmin)