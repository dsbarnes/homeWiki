from django.shortcuts import render

def index(request):
    html = 'templates/index.html'
    context = {}
    return render(request, html, context)