# from django.http import HttpResponse
from django.shortcuts import render

def homepage(request):
    # return HttpResponse("Live update on my webisite")
    return render(request, 'index.html')

def about(request):
    # return HttpResponse("This is the about page.")
    return render(request, 'index.html')

def sources(request):
    # return HttpResponse("This is the sources page.")
    return render(request, 'sources.html')