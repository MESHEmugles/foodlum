# Generated by Django 4.0.2 on 2022-02-15 10:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('foodie', '0013_remove_contact_name_remove_contact_subject_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='firstname',
            new_name='first_name',
        ),
        migrations.RenameField(
            model_name='contact',
            old_name='lastname',
            new_name='last_name',
        ),
    ]
