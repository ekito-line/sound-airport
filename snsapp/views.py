from django.shortcuts import render
from .models import Post, User

# Create your views here.


def home(request):
    return render(request, 'snsapp/home.html', {})
