# Generated by Django 4.0.1 on 2022-04-14 08:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0006_rename_expected_start_date_profile_expected_starting_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='current_year_of_study',
            field=models.CharField(blank=True, help_text='example..3rd year', max_length=10, null=True),
        ),
    ]
