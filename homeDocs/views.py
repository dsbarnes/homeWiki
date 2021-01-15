from django.http import HttpResponse, HttpResponseRedirect, FileResponse
from django.shortcuts import render, reverse, redirect
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import HomeDocs


def index(request):
    html = 'home_index.html'
    context = {}
    return render(request, html, context)

def pdf_view(request):
    # obvs don't hard code 'test.pdf'
    return FileResponse(open('test.pdf', 'rb'), as_attachment=False)

class DocsListView(LoginRequiredMixin, ListView):
    model = HomeDocs


class DocDetailView(LoginRequiredMixin, DetailView):
    model = HomeDocs


class DocCreateView(LoginRequiredMixin, CreateView):
    model = HomeDocs
    template_name_suffix = '_create_form'
    fields = ['name', 'img', 'details', 'doc_type']

    def get_success_url(self):
        doc_type = self.request.POST.get('doc_type')
        # Make this a helper function
        if doc_type == 'I':
            return reverse('inspection')
        elif doc_type == 'P':
            return reverse('purchase')
        else:
            return reverse('rooms')
    

class DocUpdateView(LoginRequiredMixin, UpdateView):
    model = HomeDocs
    template_name_suffix = '_update_form'
    fields = ['name', 'img', 'details', 'doc_type']

    def get_success_url(self):
        doc_type = self.request.POST.get('doc_type')
        if doc_type == 'I':
            return reverse('inspection')
        elif doc_type == 'P':
            return reverse('purchase')
        else:
            return reverse('rooms')


class DocDeleteView(LoginRequiredMixin, DeleteView):
    model = HomeDocs
    def get_success_url(self):
        # self.object.doc_type is 'I' / 'R' / 'P'
        if self.object.doc_type == 'I':
            return reverse('inspection')
        elif self.object.doc_type == 'P':
            return reverse('purchase')
        else:
            return rever('rooms')