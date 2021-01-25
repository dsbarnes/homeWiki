from django.shortcuts import render

# Create your views here.
def library_index(request):
    html = ''
    context = {}
    return render(request, html, context)
