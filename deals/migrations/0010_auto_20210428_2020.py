# Generated by Django 3.1.7 on 2021-04-28 08:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('deals', '0009_auto_20210428_2012'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='list',
        ),
        migrations.AddField(
            model_name='list',
            name='products',
            field=models.ManyToManyField(to='deals.Product'),
        ),
    ]
