from django.urls import path
from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import RedirectView
from django.views.generic import TemplateView


urlpatterns = [
    path('', views.index, name='index'),
    path('profile', views.profile, name='profile'),
    path('shop', views.shop, name='shop'),
    path('budget', views.budget, name='budget'),
    path('budget/<int:pk>/update/', views.BudgetUpdate.as_view(), name='budget_update'),
    path('budget/<int:pk>/delete/', views.BudgetDelete.as_view(), name='budget_delete'),
    path('budget/create', views.BudgetCreateView.as_view(), name='budget_create'),
    path('budget_product_delete/<int:pk>', views.deleteFromBudget, name='budget_product_delete'),
    path('budget/addproduct', views.AddProductView.as_view(), name='product_create'),
    path('FAQ', views.faq, name='faq'),
    path('shopping_list', views.ShoppingList.as_view(), name='shopping_list'),
    path('shopping_list/create', views.ShoppingListCreate.as_view(), name='shopping_list_create'),
    path('shopping_list/<int:pk>/update/', views.ShoppingListUpdate.as_view(), name='shopping_list_update'),
    path('shopping_list/<int:pk>/delete/', views.ShoppingListDelete.as_view(), name='shopping_list_delete'),
    path('compare_list', views.compare_list, name='compare_list'),
    path('browse', views.Browse.as_view(), name='browse'),
    path('categories', views.categories, name='categories'),
    path('details', views.details, name='details'),
    path('notification', views.notification, name='notification'),
    path('password-reset/',
         auth_views.PasswordResetView.as_view(
             template_name='registration/password_reset_form.html'), name='password_reset'),
    path('password-reset/done/',
         auth_views.PasswordResetDoneView.as_view(
             template_name='registration/password_reset_done.html'), name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(
            template_name='registration/password_reset_confirm.html'), name='password_reset_confirm'),
    path('password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(
             template_name='registration/password_reset_complete.html'), name='password_reset_complete'),
    path('register/', views.register, name='register'),
    path('staff/', views.staff, name='staff'),
    path('chartJSON', views.WeeklyBudgetChartJSON.as_view(), name='line_chart_json'),
    path('about/', views.suggestionView, name='about'),

]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
