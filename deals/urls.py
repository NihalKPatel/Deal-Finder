from django.urls import path
from django.conf.urls import url
from . import views

from .views import line_chart, line_chart_json

urlpatterns = [
    path('', views.index, name='index'),
    path('profile', views.profile, name='profile'),
    path('shop', views.shop, name='shop'),
    path('budget', views.budget, name='budget'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('shopping_list', views.shopping_list, name='shopping_list'),
    path('compare_list', views.compare_list, name='compare_list'),
    path('browse', views.browse, name='browse'),
    path('categories', views.categories, name='categories'),
    path('map', views.map, name='map'),
    path('notification', views.notification, name='notification'),
    path('register/', views.register, name='register'),
    path('analytics/', views.analytics, name='analytics'),
    path('chart', line_chart, name='line_chart'),
    path('chartJSON', line_chart_json, name='line_chart_json'),
]
