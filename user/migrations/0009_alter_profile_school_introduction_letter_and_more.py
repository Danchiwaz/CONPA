# Generated by Django 4.0.1 on 2022-04-14 08:45

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0008_alter_profile_expected_starting_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='School_introduction_Letter',
            field=models.FileField(default=2023, help_text='The letter must have an official institution stamp.', upload_to='files'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='profile',
            name='insuarance_cover',
            field=models.FileField(default=django.utils.timezone.now, upload_to='files'),
            preserve_default=False,
        ),
    ]
