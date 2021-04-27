from django.db import models
from django.contrib.auth.models import User
from django.db.models import Sum

# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    address = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.user.username} Profile'


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
    price = models.FloatField()
    location = models.CharField(max_length=255)
    list = models.ForeignKey(List, on_delete=models.CASCADE, null=False)

    @staticmethod
    def spending():
        current_spending = Product.objects.all().aggregate(sum=Sum('price'))['sum']
        return current_spending


class Budget(models.Model):
    name = models.CharField(max_length=255, default='')
    max_spend = models.FloatField()
    current_spending = models.FloatField(default=Product.spending())
    remaining_spending = models.FloatField(default=0)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, null=False)

    @staticmethod
    def spent():
        spent_done = Product.spending()
        return spent_done

    def spent_warning_amount(self):
        warning_spending = self.max_spend * 0.95
        return warning_spending

    def calculate_spending_left(self):
        left = self.max_spend - self.spent()
        self.remaining_spending = left
        return self.remaining_spending


class Category(models.Model):
    name = models.CharField(max_length=20)
    max_spend = models.IntegerField()
    budget = models.ForeignKey(Budget, on_delete=models.CASCADE, null=False)

