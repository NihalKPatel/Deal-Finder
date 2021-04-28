from django.urls import path
from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import RedirectView



urlpatterns = [
    path('', views.index, name='index'),
    path('profile', views.profile, name='profile'),
    path('shop', views.shop, name='shop'),
    path('budget', views.budget, name='budget'),
    path('budget/create', views.BudgetCreateView.as_view(), name='budget_create'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('shopping_list', views.ShoppingList.as_view(), name='shopping_list'),
    path('shopping_list/create', views.ShoppingListCreate.as_view(), name='shopping_list_create'),
    path('compare_list', views.compare_list, name='compare_list'),
    path('browse', views.browse, name='browse'),
    path('categories', views.categories, name='categories'),
    path('details', views.details, name='details'),
    path('notification', views.notification, name='notification'),
    path('register/', views.register, name='register'),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

