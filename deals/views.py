from django.http import HttpResponse

from . import utils
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from .forms import UserRegisterForm
from django.views.generic import TemplateView
from chartjs.views.lines import BaseLineChartView


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
    search = ""
    page = 1
    if request.method == 'GET':
        if 'search' in request.GET:
            search = request.GET['search']
        if 'page' in request.GET:
            page = request.GET['page']

    name_and_price = utils.get_item_search_data_nw('https://www.newworld.co.nz/shop/Search?q=' + search + '&pg=' + str(page))
    return render(request, 'pages/browse.html', {'search_results': name_and_price})


def categories(request):
    return render(request, 'pages/categories.html')


def compare_list(request):
    return render(request, 'pages/compare_list.html')


def shopping_list(request):
    return render(request, 'pages/shopping_list.html')


def map(request):
    return render(request, 'pages/map.html')


def notification(request):
    return render(request, 'pages/notification.html')


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('index')
    else:
        form = UserRegisterForm()
    return render(request, 'registration/register.html', {'form': form})

def analytics(request):
    return render(request, 'pages/analytics.html')


class LineChartJSONView(BaseLineChartView):
    def get_labels(self):
        # labels
        return ["Week 1", "Week 2", "Week 4", "Week 5", "Week 6", "Week 7"]

    def get_providers(self):
        # data to compare
        return ["Budget", "Actual spending"]

    def get_data(self):
        # data to plot
        return [
            [75, 80, 99, 44, 95, 35],
            [41, 92, 70, 39, 73, 87]
        ]


line_chart = TemplateView.as_view(template_name='line_chart.html')
line_chart_json = LineChartJSONView.as_view()