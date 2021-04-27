from django.db import models
from django.contrib.auth.models import User
from PIL import Image
# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    address = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):
        super(Profile, self).save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)


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

