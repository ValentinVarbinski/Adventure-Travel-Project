# Generated by Django 4.0.4 on 2022-04-23 09:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('at_experiences', '0003_alter_adventuretravelregistration_client'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adventuretravelexperience',
            name='category',
            field=models.CharField(choices=[('Adventure', 'Adventure'), ('Hiking', 'Hiking'), ('Sightseeing tour', 'Sightseeing tour'), ('Winter sport', 'Winter sport')], max_length=16),
        ),
    ]