# Generated by Django 3.2 on 2021-06-30 05:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('property_manager', '0005_alter_image_property'),
    ]

    operations = [
        migrations.CreateModel(
            name='Meeting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField()),
                ('property', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='meeting', to='property_manager.property')),
                ('visitor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='meeting', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]