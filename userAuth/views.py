from django.shortcuts import render, reverse
from django.contrib.auth.views import LoginView, LogoutView


class UserAuthView(LoginView):
    def get_success_url(self):
        return reverse('hidden_wiki_home')


class UserDeauthView(LogoutView):
    # b/c get_success_url, is uh... ?? wtf django?
    def get_next_page(self):
        return reverse('hidden_wiki_home')