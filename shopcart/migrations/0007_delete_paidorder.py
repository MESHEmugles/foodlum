# Generated by Django 4.0.2 on 2022-03-08 09:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shopcart', '0006_alter_paidorder_cart_no_alter_paidorder_name_on_crd_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Paidorder',
        ),
    ]
