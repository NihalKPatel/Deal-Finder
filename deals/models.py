from django.db import models
from django.contrib.auth.models import User
from django.db.models import Sum
from PIL import Image


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

    #save the image to a local directory
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
        ('W', 'Wish List'),
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

# model for storing product information
# many to many relationship with lists
class Product(models.Model):
    name = models.CharField(max_length=30)
    link = models.CharField(max_length=255, blank=True)
    price = models.FloatField()
    location = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.name

# model for storing budget information
# one budget has one list
class Budget(models.Model):
    name = models.CharField(max_length=255, default='')
    max_spend = models.FloatField(default=400)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, null=False)
    list = models.ForeignKey(List, on_delete=models.SET_NULL, null=True)

    # calculate amount at which to warn the user of their spending
    def spent_warning_amount(self):
        warning_spending = self.max_spend * 0.95
        return warning_spending

# category model to divide spending in budget for future use
class Category(models.Model):
    name = models.CharField(max_length=20)
    max_spend = models.IntegerField()
    budget = models.ForeignKey(Budget, on_delete=models.CASCADE, null=False)
