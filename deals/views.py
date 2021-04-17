from django.http import HttpResponse
from django.shortcuts import render


# HomePage
def index(request):
    return render(request, 'index.html')


def profile(request):
    return render(request, 'pages/profile.html')


def shop(request):
    return HttpResponse('shop')
