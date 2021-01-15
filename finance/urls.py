from django.urls import path
from .views import FinanceListView, FinanceDetailView, FinanceCreateView, FinanceUpdateView, FinianceDeleteView

urlpatterns = [
    path('', FinanceListView.as_view(), name='finance_list'),
    path('finance-detail/<slug:slug>', FinanceDetailView.as_view(), name='finance_detail'),

    path('finance-create/', FinanceCreateView.as_view(), name='finance_create'),
    path('finance-update/<slug:slug>', FinanceUpdateView.as_view(), name='finance_update'),
    path('finance-delete/<slug:slug>', FinianceDeleteView.as_view(), name='finance_delete'),
]
