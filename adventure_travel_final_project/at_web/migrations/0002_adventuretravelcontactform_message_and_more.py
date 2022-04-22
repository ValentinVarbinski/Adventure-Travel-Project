# Generated by Django 4.0.4 on 2022-04-18 14:11

import adventure_travel_final_project.common.validators
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('at_web', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='adventuretravelcontactform',
            name='message',
            field=models.CharField(default=1, max_length=400, validators=[adventure_travel_final_project.common.validators.validate_only_english_letters, django.core.validators.MinLengthValidator(20)]),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='adventuretravelcontactform',
            name='subject',
            field=models.CharField(max_length=40, validators=[adventure_travel_final_project.common.validators.validate_only_english_letters, django.core.validators.MinLengthValidator(5)]),
        ),
    ]