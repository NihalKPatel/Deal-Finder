from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    address = models.CharField(max_length=255, help_text="street address")  # street address
    # name = models.CharField(default=' ', max_length=100)
    #location = models.IntegerField(help_text="postcode")  # allowing to save the location by postCode

    def __str__(self):
        return f'{self.user.username} Profile'

    ## to add a method that gives the user the option to delete his/her profile
    ##def deleteProfile():


    ##add the option to re-edit the profile

class Budget(models.Model):
    default_value = 0
    max_spend = models.IntegerField(max_length=10, help_text="How much would you like to spend")
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, null=False)
    name = models.CharField(max_length=255, help_text="Budget's name")  ## budgets can be named as the user wishes


class Category(models.Model):
    name = models.CharField(primary_key=True,max_length=20)
    max_spend = models.IntegerField()
    budget = models.ForeignKey(Budget, on_delete=models.CASCADE, null=False)
    product_category = {"dairy": 0, "vegetables":0, "poultry" :0, "meat":0, "general groceries":0, "laundry":0, "personal hygiene":0}

##add a method that returns a product category
##    def category_selected(self):



    def __str__(self):
        return "{}-{}.".format(self.name, self.max_spend, self.budget)

class List(models.Model):
    TYPE = (
        ('W', 'Wish List'),
        ('S', 'Shopping List'),
    )
    type = models.CharField(
        max_length=1,
        choices=TYPE,
    )
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, null=False)


class Product(models.Model):
    name = models.CharField(max_length=30)
    link = models.CharField(max_length=255)
    price = models.IntegerField()
    location = models.CharField(max_length=255)
    list = models.ForeignKey(List, on_delete=models.CASCADE, null=False)

    # saving the product category on a dict with initial value of 0 to later modify for analytics
    # for now will do default values but these fields will need to be updated from what the user enters
    # goal of this class: to provide functionality so that the budget can be compared against the spending
    # TOOL:
class Analytics(models.Model):
    name = models.CharField(max_length=100)
    number_of_budgets = models.IntegerField()
    amount_per_budget = models.IntegerField()


