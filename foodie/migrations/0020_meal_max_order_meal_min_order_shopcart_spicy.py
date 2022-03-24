# Generated by Django 4.0.2 on 2022-02-22 12:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foodie', '0019_alter_checkout_options_alter_shopcart_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='meal',
            name='max_order',
            field=models.IntegerField(default=10),
        ),
        migrations.AddField(
            model_name='meal',
            name='min_order',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='shopcart',
            name='spicy',
            field=models.CharField(default='new', max_length=50),
        ),
    ]