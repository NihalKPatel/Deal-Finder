from django.http import HttpResponse
from django.shortcuts import render
from deals.forms import SearchForm
from . import utils


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
    form = SearchForm(request.GET)
    search = ""
    if request.method == 'GET' and 'search' in request.GET:
        search = request.GET['search']

    name_and_price = utils.get_item_search_data_nw('https://www.newworld.co.nz/shop/Search?q=' + search)
    return render(request, 'pages/browse.html', {'form': form, 'search_results': name_and_price})


def categories(request):
    return render(request, 'pages/categories.html')


def compare_list(request):
    return render(request, 'pages/compare_list.html')


def shopping_list(request):
    return render(request, 'pages/shopping_list.html')


def details(request):
    return render(request, 'pages/details.html')
