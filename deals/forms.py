from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import Form
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django.forms import ModelForm
from .models import Profile, List, userSuggestions, Budget


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


# form for creating a new product
class ProductForm(Form):
    name = forms.CharField()
    link = forms.CharField()
    price = forms.FloatField()
    location = forms.CharField()
    list = forms.ModelChoiceField(List.objects.all())

    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Submit'))
        self.helper.add_input(Submit('cancel', 'Cancel'))



#This class helps the user to upload any suggestions/comments

class userSuggestionsForm(ModelForm):
    class Meta:
        model = userSuggestions
        fields = '__all__'


class ProfileAdditionalSettings(Form):
    weekly_budget = forms.ModelChoiceField(Budget.objects.all())
