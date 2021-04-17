from django.urls import path
from . import views

urlpatterns = [
    # path('deals', views.index),
    path('', views.home, name='homepage'),
    # path('shop', views.shop),
    path('profile/', views.profile, name='profile'),
    path('profile', views.profile, name='profile'),
]
