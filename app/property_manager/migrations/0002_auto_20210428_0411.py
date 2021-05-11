# Generated by Django 3.2 on 2021-04-28 04:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property_manager', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='property',
            name='adress',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='property',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='property',
            name='latitude',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='property',
            name='longitude',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='property',
            name='price',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='property',
            name='surface',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]