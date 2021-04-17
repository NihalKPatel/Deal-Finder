from django.http import HttpResponse
from django.shortcuts import render


# HomePage
def index(request):
    return render(request, 'index.html')


def profile(request):
    return render(request, 'pages/profile.html')


def shop(request):
    return render(request, 'pages/shop.html')


def dashboard(request):
    return render(request, 'pages/dashboard.html')


def budget(request):
    return render(request, 'pages/budget.html')


def browse(request):
    return render(request, 'pages/browse.html')


def categories(request):
    return render(request, 'pages/categories.html')


def compare_list(request):
    return render(request, 'pages/compare_list.html')


def shopping_list(request):
    return render(request, 'pages/shopping_list.html')


def map(request):
    return render(request, 'pages/map.html')
