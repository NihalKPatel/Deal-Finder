from django.db import models
from django.contrib.auth.models import User
from django.db.models import Sum
from PIL import Image
from datetime import datetime


# Create your models here.

# model for storing unique user data that isnt included
# in the django authentication user
class Profile(models.Model):
    # one user has one profile
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    address = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.user.username} Profile'

    # save the image to a local directory
    def save(self, *args, **kwargs):
        super(Profile, self).save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)


# model for storing list names and list types
# many to many relationship with products so many lists
# can have many products
class List(models.Model):
    name = models.CharField(max_length=30, default="default name")
    # possible choices for types of lists
    TYPE = (
        ('W', 'Watch List'),
        ('S', 'Shopping List'),
    )
    type = models.CharField(
        max_length=1,
        choices=TYPE,
    )
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, null=False)
    products = models.ManyToManyField('Product', )

    def __str__(self):
        return self.name

    def total(self):
        queryset = self.products.all().aggregate(total_price=models.Sum('price'))['total_price']
        return queryset

# model for storing product information
# many to many relationship with lists
class Product(models.Model):
    name = models.CharField(max_length=50)
    link = models.CharField(max_length=255, blank=True)
    price = models.FloatField()
    location = models.CharField(max_length=255, blank=True)
    product_type = models.IntegerField(blank=True, default=1)

    def __str__(self):
        return self.name


# model for storing budget information
# one budget has one list
class Budget(models.Model):
    name = models.CharField(max_length=255, default='')
    max_spend = models.FloatField(default=400)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, null=False)
    list = models.ForeignKey(List, on_delete=models.SET_NULL, null=True, blank=True)
    # whether this is the users chosen weekly budget
    weekly = models.BooleanField(default=False)
    # blank if you don't want this budget to appear on analytics
    date = models.DateField(default=None, null=True, blank=True)

    # calculate amount at which to warn the user of their spending
    def spent_warning_amount(self):
        warning_spending = self.max_spend * 0.95
        return warning_spending

    # sum of values of all products in this budgets list
    def spent(self):
        spent = 0
        if self.list is None:
            return 0
        products = self.list.products.all()
        for product in products:
            spent += product.price
        return spent

    def __str__(self):
        return self.name


# category model to divide spending in budget for future use
class Category(models.Model):
    name = models.CharField(max_length=20)
    max_spend = models.IntegerField()
    budget = models.ForeignKey(Budget, on_delete=models.CASCADE, null=False)


class userSuggestions(models.Model):
    name = models.CharField(max_length=50)
    contact_email = models.EmailField()
    comment_suggestion = models.TextField(max_length=600)

    def __str__(self):
        return self.name + " " + self.contact_email + " " + self.comment_suggestion
