from django.contrib import admin
from .models import Profile, Budget, Category, List, Product, userSuggestions

admin.site.register(Profile)
admin.site.register(Budget)
admin.site.register(Category)
admin.site.register(List)
admin.site.register(Product)
admin.site.register(userSuggestions)

