from django.shortcuts import render
from django.http import HttpResponse


def dashboard(request):
    return HttpResponse('<h1>This is the dashboard</h1>')


def profile(request):
    return HttpResponse('<h1>This is the profile page</h1>')


def shopping(request):
    return HttpResponse('<h1>This is the shopping page</h1>')


def budget(request):
    return HttpResponse('<h1>This is the budget page</h1>')


def mapping(request):
    return HttpResponse('<h1>This is the maps page</h1>')
