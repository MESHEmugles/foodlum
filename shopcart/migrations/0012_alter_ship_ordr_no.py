# Generated by Django 4.0.2 on 2022-03-24 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopcart', '0011_alter_ship_meal'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ship',
            name='ordr_no',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
