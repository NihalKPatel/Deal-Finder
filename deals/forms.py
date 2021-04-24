from django import forms
from mapwidgets.widgets import GoogleStaticMapWidget, GoogleStaticOverlayMapWidget, GooglePointFieldWidget
from django.contrib.gis.db import models
from django.contrib.gis.geos import Point

from deals.models import Location

DEFAULT_LOCATION_POINT = Point(-104.9903, 39.7392)


class SearchForm(forms.Form):
    search = forms.CharField(help_text="Search here!")


class CityCreateForm(forms.ModelForm):
    class Meta:
        model = Location
        fields = ('name', 'location')
        widgets = {
            'location': GooglePointFieldWidget,
        }


class CityDetailForm(forms.ModelForm):
    class Meta:
        model = Location
        fields = ('name', 'location')
        widgets = {
            'location': GoogleStaticOverlayMapWidget(zoom=12, thumbnail_size='50x50', size='640x640'),
        }
