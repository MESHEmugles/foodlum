# Generated by Django 4.0.2 on 2022-03-03 10:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shopcart', '0003_alter_checkout_admin_remark_alter_checkout_status_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Paidorder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('checkout', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shopcart.checkout')),
            ],
            options={
                'verbose_name': 'Paidorder',
                'verbose_name_plural': 'Paidorders',
                'db_table': 'paidorder',
                'managed': True,
            },
        ),
    ]
