from django.shortcuts import render, reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Finance
from .forms import FinanceForm
from datetime import datetime


class FinanceListView(LoginRequiredMixin, ListView):
    model = Finance 

class FinanceDetailView(LoginRequiredMixin, DetailView):
    model = Finance


class FinanceCreateView(LoginRequiredMixin, CreateView):
    model = Finance
    template_name_suffix = '_create_form'
    form_class = FinanceForm

    def get_success_url(self):
        return reverse('finance_list')


class FinanceUpdateView(LoginRequiredMixin, UpdateView):
    model = Finance
    template_name_suffix = '_update_form'
    form_class = FinanceForm
    # fields = ['name', 'amount', 'date', 'finance_type']

    def get_success_url(self):
        return reverse('finance_list')


class FinianceDeleteView(LoginRequiredMixin, DeleteView):
    model = Finance

    def get_success_url(self):
        return reverse('finance_list')