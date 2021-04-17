from django.db import models


class shop(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField()
    # stock = models.integerField()



