# Generated by Django 4.0.2 on 2022-03-08 12:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopcart', '0008_ship_paidorder'),
    ]

    operations = [
        migrations.AddField(
            model_name='ship',
            name='phone',
            field=models.IntegerField(default=1),
        ),
    ]
