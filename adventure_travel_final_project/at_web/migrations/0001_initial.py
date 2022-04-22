# Generated by Django 4.0.4 on 2022-04-18 14:08

import adventure_travel_final_project.common.validators
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AdventureTravelContactForm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=40, validators=[adventure_travel_final_project.common.validators.validate_only_english_letters, django.core.validators.MinLengthValidator(5)])),
                ('subject', models.CharField(max_length=400, validators=[adventure_travel_final_project.common.validators.validate_only_english_letters, django.core.validators.MinLengthValidator(20)])),
                ('replied', models.BooleanField(default=False)),
                ('date_received', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Contact Form',
            },
        ),
    ]