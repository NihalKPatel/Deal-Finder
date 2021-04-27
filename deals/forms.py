from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
# create a new form that inherits from UserCreationForm
from django.forms import ModelForm
from .models import Product


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class CreateNewProduct(ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
