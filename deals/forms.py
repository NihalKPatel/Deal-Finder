from django import forms


class SearchForm(forms.Form):
    search = forms.CharField(help_text="Search here!")
