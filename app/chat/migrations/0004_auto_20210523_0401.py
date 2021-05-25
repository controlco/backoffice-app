# Generated by Django 3.2 on 2021-05-23 04:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0003_auto_20210523_0224'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='read',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='message',
            name='subject',
            field=models.CharField(default='[Sin Asunto]', max_length=100),
        ),
    ]