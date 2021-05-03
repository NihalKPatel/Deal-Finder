from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import Form

from .models import Profile, List

# form for creating a user
class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

# form for updating a user
class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']

# form for updating a profile
class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']

#form for creating a new product
class ProductForm(Form):
    name = forms.CharField()
    link = forms.CharField()
    price = forms.FloatField()
    location = forms.CharField()
    list = forms.ModelChoiceField(List.objects.all())
