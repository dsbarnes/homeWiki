from django.contrib import admin
from django.urls import path, include
from .views import index
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', index, name='hidden_wiki_home'),
    path('home/', include('homeDocs.urls')),
    path('finance/', include('finance.urls')),
    path('recipes/', include('recipes.urls')),
    path('storage/', include('storage.urls')),
    path('grocery/', include('grocery.urls')),
    path('auth/', include('userAuth.urls')),
] 
