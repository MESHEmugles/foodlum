# Generated by Django 4.0.2 on 2022-02-15 09:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foodie', '0012_remove_meal_spicy_alter_contact_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='name',
        ),
        migrations.RemoveField(
            model_name='contact',
            name='subject',
        ),
        migrations.AddField(
            model_name='contact',
            name='email',
            field=models.EmailField(default='new', max_length=100),
        ),
        migrations.AddField(
            model_name='contact',
            name='firstname',
            field=models.CharField(default='new', max_length=100),
        ),
        migrations.AddField(
            model_name='contact',
            name='lastname',
            field=models.CharField(default='new', max_length=100),
        ),
        migrations.AlterField(
            model_name='contact',
            name='closed',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]