from . import utils
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import List, Profile, Product, Budget
from django.views import generic
from django.urls import reverse, reverse_lazy
from django.contrib import messages
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required


# HomePage
def index(request):
    return render(request, 'index.html')


def profile(request):
    return render(request, 'pages/profile.html')


def shop(request):
    return render(request, 'pages/shop.html')


def dashboard(request):
    return render(request, 'pages/dashboard.html')


@login_required(login_url='/accounts/login/')
def budget(request):
    total_spent = 0
    index = 1
    if request.method == 'GET':
        if 'budget' in request.GET:
            index = int(request.GET['budget'])
    budgets = Budget.objects.filter(profile_id=request.user.id)
    if budgets.count() <= 0:
        return redirect('budget_create')

    current_budget = Budget.objects.filter(profile_id=request.user.id)[index - 1]
    budget_list = List.objects.get(budget=current_budget.id)

    products = budget_list.products.all()
    print(products)
    for product in products:
        total_spent += product.price

    money_remaining = current_budget.max_spend - total_spent
    return render(request, 'pages/budget.html', {'products': products,
                                                 'budget': current_budget,
                                                 'all_budgets': budgets,
                                                 'money_spent': total_spent,
                                                 'money_remaining': money_remaining
                                                 })


# @login_required(login_url='/accounts/login/')
# def browse(request):
#     search = ""
#     page = 1
#     if request.method == 'GET':
#         if 'search' in request.GET:
#             search = request.GET['search']
#         if 'page' in request.GET:
#             page = request.GET['page']
#
#     name_and_price = utils.get_item_search_data_nw(
#         'https://www.newworld.co.nz/shop/Search?q=' + search + '&pg=' + str(page))
#     return render(request, 'pages/browse.html', {'search_results': name_and_price})


class Browse(LoginRequiredMixin, generic.ListView):
    model = Product
    template_name = 'pages/browse.html'
    paginate_by = 20
    login_url = '/accounts/login/'

    def get_queryset(self):
        if self.request.method == 'GET' and 'search' in self.request.GET:
            search = self.request.GET['search']
            return Product.objects.filter(name__icontains=search)
        else:
            return Product.objects.all()

    def post(self, request, *args, **kwargs):
            if 'product' in self.request.POST and 'list' in self.request.POST:
                product_id = self.request.POST['product']
                list_id = self.request.POST['list']
                print('List: ' + list_id)
                print('Product: ' + product_id)
                List.objects.get(id=list_id).products.add(Product.objects.get(id=product_id))
                print(self.extra_context)
            return render(request, self.template_name)

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        if self.request.method == 'GET' and 'search' in self.request.GET:
            search = self.request.GET['search']
            context['search'] = search
        else:
            context['search'] = ''

        context['all_lists'] = List.objects.filter(profile_id=self.request.user.id)
        return context


def categories(request):
    return render(request, 'pages/categories.html')


def compare_list(request):
    return render(request, 'pages/compare_list.html')


class ShoppingList(LoginRequiredMixin, generic.ListView):
    model = List
    template_name = 'pages/shopping_list.html'
    context_object_name = 'shopping_lists'


class ShoppingListCreate(LoginRequiredMixin, CreateView):
    model = List
    template_name = 'pages/shopping_list_create.html'
    fields = ['name']
    success_url = reverse_lazy('shopping_list')

    def form_valid(self, form):
        form.instance.profile = Profile.objects.filter(user_id=self.request.user.id)[0]
        form.instance.type = 'S'
        return super().form_valid(form)


class ShoppingListUpdate(LoginRequiredMixin, UpdateView):
    model = List
    template_name = 'pages/shopping_list_update.html'
    fields = ['name']
    success_url = reverse_lazy('shopping_list')


class ShoppingListDelete(LoginRequiredMixin, DeleteView):
    model = List
    template_name = 'pages/shopping_list_delete.html'
    success_url = reverse_lazy('shopping_list')


class BudgetCreateView(LoginRequiredMixin, CreateView):
    model = Budget
    template_name = 'pages/budget_create.html'
    fields = ['name', 'max_spend', 'list']
    success_url = reverse_lazy('budget')

    def form_valid(self, form):
        form.instance.profile = Profile.objects.filter(user_id=self.request.user.id)[0]
        return super().form_valid(form)


class BudgetUpdate(LoginRequiredMixin, UpdateView):
    model = Budget
    template_name = 'pages/shopping_list_update.html'
    fields = ['name', 'max_spend', 'list']
    success_url = reverse_lazy('budget')


class BudgetDelete(LoginRequiredMixin, DeleteView):
    model = Budget
    template_name = 'pages/shopping_list_delete.html'
    success_url = reverse_lazy('budget')


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


@staff_member_required(redirect_field_name='/accounts/login/')
def staff(request):
    if request.method == 'POST' and 'scrape' in request.POST:
        utils.scrape_all_products()

    return render(request, 'pages/staff.html')
