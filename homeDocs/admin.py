from django.contrib import admin
from .models import HomeDocs

# Register your models here.
class HomeDocsAdmin(admin.ModelAdmin):
    fields = ['name', 'media', 'details', 'doc_type', 'slug']
    prepopulated_fields = {'slug': ('name', )}

admin.site.register(HomeDocs, HomeDocsAdmin)