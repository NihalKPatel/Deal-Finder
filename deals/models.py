from django.db import models
from django.contrib.auth.models import User
from django.contrib.gis.db.models import PointField
from django.contrib.gis.db import models


# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    address = models.CharField(max_length=255)


class Budget(models.Model):
    max_spend = models.IntegerField()
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, null=False)


class Category(models.Model):
    name = models.CharField(max_length=20)
    max_spend = models.IntegerField()
    budget = models.ForeignKey(Budget, on_delete=models.CASCADE, null=False)


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


class Location(models.Model):
    name = models.CharField(max_length=255)
    location = models.PointField(help_text="Use map widget for point the house location")

    def __str__(self):
        return self.name
