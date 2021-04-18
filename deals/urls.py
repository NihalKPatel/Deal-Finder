from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='deals-dashboard'),
    path('profile/', views.profile, name='deals-profile'),
    path('shop/', views.shopping, name='deals-shopping'),
    path('budget/', views.budget, name='deals-budget'),
    path('mappings/', views.mapping, name='deals-mapping'),
]