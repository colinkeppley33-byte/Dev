from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def articles_page(request):
    return render(request, 'articles/articles.html')