# Generated by Django 4.0.2 on 2022-02-24 09:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('foodie', '0020_meal_max_order_meal_min_order_shopcart_spicy'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='checkout',
            name='shopcart',
        ),
        migrations.DeleteModel(
            name='contact',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='user',
        ),
        migrations.RemoveField(
            model_name='shopcart',
            name='meal',
        ),
        migrations.RemoveField(
            model_name='shopcart',
            name='user',
        ),
        migrations.DeleteModel(
            name='Checkout',
        ),
        migrations.DeleteModel(
            name='Profile',
        ),
        migrations.DeleteModel(
            name='Shopcart',
        ),
    ]
