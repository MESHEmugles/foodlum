# Generated by Django 4.0.2 on 2022-03-07 09:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UContact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, max_length=100, null=True)),
                ('last_name', models.CharField(blank=True, max_length=100, null=True)),
                ('email', models.EmailField(blank=True, max_length=100, null=True)),
                ('phone', models.CharField(blank=True, max_length=100, null=True)),
                ('message', models.TextField(blank=True, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(choices=[('New', 'New'), ('Pending', 'Pending'), ('Process', 'Process'), ('closed', 'Closed')], default='new', max_length=100)),
                ('closed', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'UContact',
                'verbose_name_plural': 'UContacts',
                'db_table': 'ucontact',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='UProfile',
            fields=[
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
                ('phone', models.CharField(blank=True, max_length=100, null=True)),
                ('address', models.CharField(blank=True, max_length=100, null=True)),
                ('state', models.CharField(blank=True, max_length=40, null=True)),
                ('image', models.ImageField(blank=True, default='profile.jpg', null=True, upload_to='profile')),
                ('city', models.CharField(max_length=100)),
                ('zip', models.IntegerField()),
                ('cart_code', models.AutoField(default=101, primary_key=True, serialize=False)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'UProfile',
                'verbose_name_plural': 'UProfiles',
                'db_table': 'uprofile',
                'managed': True,
            },
        ),
    ]