# Generated by Django 4.0.2 on 2022-02-22 10:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('foodie', '0017_alter_profile_image_alter_profile_phone'),
    ]

    operations = [
        migrations.CreateModel(
            name='Shopcart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('spicy', models.CharField(max_length=100)),
                ('order_no', models.CharField(max_length=50)),
                ('item_paid', models.BooleanField(default=False)),
                ('meal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='foodie.meal')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Checkout',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ordr_no', models.CharField(max_length=50)),
                ('itm_paid', models.BooleanField(default=False)),
                ('total', models.FloatField()),
                ('address', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=50)),
                ('zip', models.IntegerField()),
                ('name_on_card', models.CharField(max_length=200)),
                ('card_number', models.IntegerField()),
                ('cvv', models.IntegerField()),
                ('month', models.CharField(max_length=50)),
                ('shopcart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='foodie.shopcart')),
            ],
        ),
    ]
