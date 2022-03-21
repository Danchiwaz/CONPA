# Generated by Django 4.0.1 on 2022-03-17 12:51

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
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstName', models.CharField(max_length=100)),
                ('lastName', models.CharField(max_length=100)),
                ('universityName', models.CharField(max_length=300)),
                ('level_of_Education', models.CharField(choices=[('Diploma', 'Diploma'), ('Bachelors Degree', 'Bachelors Degree')], max_length=200)),
                ('course_name', models.CharField(max_length=300)),
                ('files', models.FileField(upload_to='files/%Y/%m/%d')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]