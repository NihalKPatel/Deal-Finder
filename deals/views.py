from django.shortcuts import render
from django.http import HttpResponse


def dashboard(request):
    return HttpResponse('<h1>This is the dashboard</h1>')
