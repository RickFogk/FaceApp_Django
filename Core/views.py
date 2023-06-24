from django.shortcuts import render
from django.http import HttpResponse
from .forms import ProfileForm


# Create your views here.
def index(request):
    return render(request, 'Core/index.html')

def profile(request):
    form = ProfileForm()
    return render(request, 'Core/profile.html', {'form': form})

def post(request):
    return render(request, 'Core/post.html')
