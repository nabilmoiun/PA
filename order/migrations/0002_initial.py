# Generated by Django 4.2.7 on 2023-11-26 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('shopping_cart', '0001_initial'),
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='items',
            field=models.ManyToManyField(to='shopping_cart.shop'),
        ),
    ]
