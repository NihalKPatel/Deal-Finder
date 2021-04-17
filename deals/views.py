from django.http import HttpResponse
from django.shortcuts import render


# HomePage
def index(request):
    return HttpResponse('Homepage')

def home(request):
    return render(request, 'home/home.html')


def profile(request):
    return render(request, 'profile.html')


def shop(request):
    return HttpResponse('shop')
