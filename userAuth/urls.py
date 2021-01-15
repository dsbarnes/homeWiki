from django.urls import path
from .views import UserAuthView, UserDeauthView

urlpatterns = [
    path('login', UserAuthView.as_view(), name='login'),
    path('logout', UserDeauthView.as_view(), name='logout'),
]