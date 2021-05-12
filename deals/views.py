from django.http import HttpResponse

from . import scraper
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from .models import List, Profile, Product, Budget
from django.views import generic
from django.urls import reverse, reverse_lazy
from django.contrib import messages
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm, ProductForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from .forms import UserRegisterForm
from chartjs.views.lines import BaseLineChartView


# View to handle the index template
def index(request):
    return render(request, 'index.html')


# View to handle the shop template
def shop(request):
    return render(request, 'pages/shop.html')


# View to handle the dashboard template
def dashboard(request):
    return render(request, 'pages/dashboard.html')


# View to handle the budget template and process GET requests
@login_required(login_url='/accounts/login/')
def budget(request):
    total_spent = 0
    # use first budget by default
    index = 1

    # if the http request specifies which budget to view
    if request.method == 'GET':
        if 'budget' in request.GET:
            index = int(request.GET['budget'])
    budgets = Budget.objects.filter(profile_id=request.user.id)

    # if the user has no budgets redirect to the create budget page
    if budgets.count() <= 0:
        return redirect('budget_create')

    # Find the budget for that particular user with the index specified
    current_budget = Budget.objects.filter(profile_id=request.user.id)[index - 1]
    # find the single list that belongs to that budget
    budget_list = List.objects.get(budget=current_budget.id)

    products = budget_list.products.all()
    print(products)
    # increment total money spent for the price of each item
    for product in products:
        total_spent += product.price

    money_remaining = current_budget.max_spend - total_spent
    return render(request, 'pages/budget.html', {'products': products,
                                                 'budget': current_budget,
                                                 'all_budgets': budgets,
                                                 'money_spent': total_spent,
                                                 'money_remaining': money_remaining
                                                 })


# View to handle the browse template and process GET and POST requests
class Browse(LoginRequiredMixin, generic.ListView):
    model = Product
    template_name = 'pages/browse.html'
    paginate_by = 20
    login_url = '/accounts/login/'

    # use GET requests to filter the product items for the listview
    # and pass the previous search into the current page so it isn't lost
    def get_queryset(self):
        if self.request.method == 'GET' and 'search' in self.request.GET:
            search = self.request.GET['search']
            return Product.objects.filter(name__icontains=search)
        else:
            return Product.objects.all()

    # use POST requests to handle adding products to lists
    def post(self, request, *args, **kwargs):
        if 'product' in self.request.POST and 'list' in self.request.POST:
            product_id = self.request.POST['product']
            list_id = self.request.POST['list']
            List.objects.get(id=list_id).products.add(Product.objects.get(id=product_id))
            print(self.extra_context)
        return redirect(reverse_lazy('shopping_list'))

    # add previous search text into the current page so u maintain ur
    # search in the search bar when the page refreshes
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


# View to handle the categories template
def categories(request):
    return render(request, 'pages/categories.html')


# View to handle the compare list template
def compare_list(request):
    return render(request, 'pages/compare_list.html')


# list view to display all of the users lists
class ShoppingList(LoginRequiredMixin, generic.ListView):
    model = List
    template_name = 'pages/shopping_list.html'
    context_object_name = 'shopping_lists'

    def post(self, request, *args, **kwargs):
        if 'list' in request.POST and 'product' in request.POST:
            product = Product.objects.get(id=request.POST['product'])
            List.objects.get(id=request.POST['list']).products.remove(product)
        return redirect(reverse_lazy('shopping_list'))

    def get_queryset(self):
        return List.objects.filter(profile_id=self.request.user.id)


# generic create view for creating shopping lists
class ShoppingListCreate(LoginRequiredMixin, CreateView):
    model = List
    template_name = 'pages/shopping_list_create.html'
    fields = ['name']
    success_url = reverse_lazy('shopping_list')

    # ensure the form adds the current user to the newly created list
    def form_valid(self, form):
        form.instance.profile = Profile.objects.get(user_id=self.request.user.id)
        form.instance.type = 'S'
        return super().form_valid(form)

# generic update view for updating lists
class ShoppingListUpdate(LoginRequiredMixin, UpdateView):
    model = List
    template_name = 'pages/shopping_list_update.html'
    fields = ['name']
    success_url = reverse_lazy('shopping_list')

# generic delete view for deleting lists
class ShoppingListDelete(LoginRequiredMixin, DeleteView):
    model = List
    template_name = 'pages/shopping_list_delete.html'
    success_url = reverse_lazy('shopping_list')


# form view for adding products to lists
class AddProductView(FormView):
    template_name = "pages/product_create.html"
    form_class = ProductForm

    #if the form is valid create the new product and add it to a list
    def form_valid(self, form):
        name = form.cleaned_data['name']
        link = form.cleaned_data['link']
        price = form.cleaned_data['price']
        location = form.cleaned_data['location']
        list = form.cleaned_data['list']
        product = Product(name=name, link=link, price=price, location=location)
        product.save()
        List.objects.get(name=list).products.add(Product.objects.get(id=product.id))
        return redirect(reverse_lazy('budget'))

# generic create view for creating a budget
class BudgetCreateView(CreateView):
    model = Budget
    template_name = 'pages/budget_create.html'
    fields = ['name', 'max_spend', 'list']
    success_url = reverse_lazy('budget')

    # ensure the form adds the current user to the newly created budget
    def form_valid(self, form):
        form.instance.profile = Profile.objects.get(user_id=self.request.user.id)
        return super().form_valid(form)

    # ensures you can only create a budget with your own shopping list
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'].fields['list'].queryset = List.objects.filter(profile_id=self.request.user.id)
        return context

# generic update view for updating budgets
class BudgetUpdate(LoginRequiredMixin, UpdateView):
    model = Budget
    template_name = 'pages/shopping_list_update.html'
    fields = ['name', 'max_spend', 'list']
    success_url = reverse_lazy('budget')

    # ensures you can only create a budget with your own shopping list
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'].fields['list'].queryset = List.objects.filter(profile_id=self.request.user.id)
        return context

# generic delete view for deleting budgets
class BudgetDelete(LoginRequiredMixin, DeleteView):
    model = Budget
    template_name = 'pages/shopping_list_delete.html'
    success_url = reverse_lazy('budget')

# view to handle the details template
def details(request):
    return render(request, 'pages/details.html')

# view to handle the notifications template
def notification(request):
    return render(request, 'pages/notification.html')

# view to handle the register form, using POST http requests for security
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

# view to handle viewing of the profile
# also acting as an updateview for the profile on the same page
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

# view only accessible to staff members (currently the superuser) allowing you to scrape data
# from your chosen store in one click and storing it in the database
@staff_member_required(redirect_field_name='/accounts/login/')
def staff(request):
    if request.method == 'POST' and 'scrape' in request.POST:
        scraper.scrape_all_products()

    return render(request, 'pages/staff.html')

# view to handle the analytics template
def analytics(request):
    return render(request, 'pages/analytics.html')

# view to handle the chart
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
