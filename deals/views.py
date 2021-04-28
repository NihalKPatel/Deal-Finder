from . import utils
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import List, Profile, Product, Budget
from django.views import generic
from django.urls import reverse, reverse_lazy
from django.contrib import messages
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from django.contrib.auth.decorators import login_required


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
    total_spent = 0
    index = 1
    if request.method == 'GET':
        if 'budget' in request.GET:
            index = int(request.GET['budget'])
    budgets = Budget.objects.filter(profile_id=request.user.id)
    if budgets.count() <= 0:
        return BudgetCreateView.as_view()

    current_budget = Budget.objects.filter(profile_id=request.user.id)[index-1]
    products = Product.objects.filter(list_id=current_budget.list_id)
    for product in products:
        total_spent += product.price

    money_remaining = current_budget.max_spend-total_spent
    return render(request, 'pages/budget.html', {'products': products,
                                                 'budget': current_budget,
                                                 'all_budgets': budgets,
                                                 'money_spent': total_spent,
                                                 'money_remaining': money_remaining
                                                 })


def browse(request):
    search = ""
    page = 1
    budgets = Budget.objects.filter(profile_id=request.user.id)
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


class ShoppingList(generic.ListView):
    model = List
    template_name = 'pages/shopping_list.html'
    context_object_name = 'shopping_lists'


class ShoppingListCreate(CreateView):
    model = List
    template_name = 'pages/shopping_list_create.html'
    fields = ['name']
    success_url = reverse_lazy('shopping_list')

    def form_valid(self, form):
        form.instance.profile = Profile.objects.filter(user_id=self.request.user.id)[0]
        return super().form_valid(form)


class BudgetCreateView(CreateView):
    model = Budget
    template_name = 'pages/budget_create.html'
    fields = ['name', 'max_spend', 'list']
    success_url = reverse_lazy('budget')

    def form_valid(self, form):
        form.instance.profile = Profile.objects.filter(user_id=self.request.user.id)[0]
        return super().form_valid(form)


def details(request):
    return render(request, 'pages/details.html')


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


@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!!')
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request, 'pages/profile.html', context)
