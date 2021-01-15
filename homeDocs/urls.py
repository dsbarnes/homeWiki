from django.urls import path 
from .views import index, pdf_view, DocsListView, DocDetailView, DocCreateView, DocUpdateView, DocDeleteView

urlpatterns = [
    path('', index, name='home_index'),

    path('inspection/', DocsListView.as_view(template_name='inspection_list.html'), name='inspection'),
    path('inspection/<slug:slug>', DocDetailView.as_view()),

    path('purchase/', DocsListView.as_view(template_name='purchase_list.html'), name='purchase'),
    path('purchase/<slug:slug>', DocDetailView.as_view()),

    path('rooms/', DocsListView.as_view(template_name='rooms_list.html'), name='rooms'),
    path('rooms/<slug:slug>', DocDetailView.as_view()),

    path('homedoc-create/', DocCreateView.as_view(), name='doc_create'),
    path('homedoc-update/<slug:slug>', DocUpdateView.as_view(), name='doc_update'),
    path('confirm-delete/<slug:slug>', DocDeleteView.as_view(), name='doc_delete'),

    path('pdf-view/', pdf_view, name='pdf'),
    # path('img-view<slug:slug>/', img_view, name='img'),
]
