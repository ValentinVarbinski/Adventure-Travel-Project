# Generated by Django 4.0.4 on 2022-04-20 09:17

import adventure_travel_final_project.common.validators
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('at_web', '0002_adventuretravelcontactform_message_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adventuretravelcontactform',
            name='message',
            field=models.TextField(max_length=400, validators=[adventure_travel_final_project.common.validators.validate_only_english_letters, django.core.validators.MinLengthValidator(20)]),
        ),
    ]