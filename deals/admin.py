from django.contrib import admin

from . import models
from .models import Profile, Budget, Category, List, Product
from mapwidgets.widgets import GooglePointFieldWidget, GooglePointFieldInlineWidget, GoogleStaticMapWidget, GoogleStaticOverlayMapWidget
from django.contrib.gis.db import models

admin.site.register(Profile)
admin.site.register(Budget)
admin.site.register(Category)
admin.site.register(List)
admin.site.register(Product)


class CityAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.PointField: {"widget": GoogleStaticMapWidget}
    }
