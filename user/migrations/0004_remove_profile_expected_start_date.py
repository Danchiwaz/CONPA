# Generated by Django 4.0.1 on 2022-04-14 08:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_remove_profile_files'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='expected_start_date',
        ),
    ]
