# Generated by Django 4.0.1 on 2022-04-14 08:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_remove_profile_expected_start_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='expected_start_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
