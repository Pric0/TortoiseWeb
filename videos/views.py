from django.shortcuts import render
from django.http import HttpResponse

from .models import Movies

# Create your views here.
def index(request):
    movies = Movies.objects
    return render(request, 'videos\index.html')