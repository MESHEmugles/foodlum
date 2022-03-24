# Generated by Django 4.0.2 on 2022-03-01 09:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopcart', '0002_remove_shopcart_spicy_shopcart_now_spicy'),
    ]

    operations = [
        migrations.AlterField(
            model_name='checkout',
            name='admin_remark',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='checkout',
            name='status',
            field=models.CharField(choices=[('New', 'New'), ('Pending', 'Pending'), ('Processing', 'Processing'), ('Shipping', 'Shipping'), ('Delivered', 'Delivered')], max_length=50),
        ),
        migrations.AlterField(
            model_name='shopcart',
            name='now_spicy',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='shopcart',
            name='product_name',
            field=models.CharField(max_length=100),
        ),
    ]