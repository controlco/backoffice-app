from django.db import models
from accounts.models import User
# Create your models here.


class Region(models.Model):
    name = models.TextField()
    number = models.PositiveIntegerField(primary_key=True)


class District(models.Model):
    name = models.TextField()
    region = models.ForeignKey(
        Region, on_delete=models.CASCADE, related_name="district")


class Property(models.Model):
    title = models.TextField()
    owner = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="property")
    surface = models.PositiveIntegerField(blank=True, null=True)
    adress = models.TextField(blank=True, null=True)
    price = models.PositiveIntegerField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    latitude = models.CharField(max_length=50, blank=True, null=True)
    longitude = models.CharField(max_length=50, blank=True, null=True)
    is_active = models.BooleanField(
        default=False, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')
    district = models.ForeignKey(
        District, on_delete=models.CASCADE, related_name="property")
