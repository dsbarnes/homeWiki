from django.shortcuts import render

# Create your views here.
def index(request):
    html = 'storage.html'
    context = {}
    return render(request, html, context)
