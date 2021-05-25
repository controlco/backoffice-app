# Generated by Django 3.2 on 2021-05-25 05:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property_manager', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='property',
            name='electricity_service',
            field=models.BooleanField(default=False, help_text='Designates whether this property has electricity service. Unselect this instead of deleting accounts.', verbose_name='electricity'),
        ),
        migrations.AddField(
            model_name='property',
            name='water_service',
            field=models.BooleanField(default=False, help_text='Designates whether this property has drinking water service. Unselect this instead of deleting accounts.', verbose_name='water'),
        ),
    ]