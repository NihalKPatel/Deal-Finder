from django.http import HttpResponse
from django.shortcuts import render


# HomePage
def index(request):
    return HttpResponse('Homepage')
