from django.urls import path
from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import RedirectView
from django.views.generic import TemplateView


urlpatterns = [
    path('', views.index, name='index'),
    path('profile', views.profile, name='profile'),
    path('about/', views.about, name='about'),
    path('shop', views.shop, name='shop'),
    path('budget', views.budget, name='budget'),
    path('budget/<int:pk>/update/', views.BudgetUpdate.as_view(), name='budget_update'),
    path('budget/<int:pk>/delete/', views.BudgetDelete.as_view(), name='budget_delete'),
    path('budget/create', views.BudgetCreateView.as_view(), name='budget_create'),
    path('budget/addproduct', views.AddProductView.as_view(), name='product_create'),
    path('faq', views.faq, name='faq'),
    path('shopping_list', views.ShoppingList.as_view(), name='shopping_list'),
    path('shopping_list/create', views.ShoppingListCreate.as_view(), name='shopping_list_create'),
    path('shopping_list/<int:pk>/update/', views.ShoppingListUpdate.as_view(), name='shopping_list_update'),
    path('shopping_list/<int:pk>/delete/', views.ShoppingListDelete.as_view(), name='shopping_list_delete'),
    path('compare_list', views.compare_list, name='compare_list'),
    path('browse', views.Browse.as_view(), name='browse'),
    path('categories', views.categories, name='categories'),
    path('details', views.details, name='details'),
    path('notification', views.notification, name='notification'),
    path('register/', views.register, name='register'),
    path('staff/', views.staff, name='staff'),
    path('contactUs/', views.suggestionView, name='contactUs'),

]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
