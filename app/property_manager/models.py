from django.db import models
from django.db.models.enums import Choices
from accounts.models import User
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.


class Region(models.Model):
    name = models.TextField()
    number = models.PositiveIntegerField(primary_key=True)

    def __str__(self):
        return self.name


class District(models.Model):
    name = models.TextField()
    region = models.ForeignKey(
        Region, on_delete=models.CASCADE, related_name="district")

    def __str__(self):
        return self.name


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
    electricity_service = models.BooleanField(
        default=False, help_text='Designates whether this property has electricity service. Unselect this instead of deleting accounts.', verbose_name='electricity')
    water_service = models.BooleanField(
        default=False, help_text='Designates whether this property has drinking water service. Unselect this instead of deleting accounts.', verbose_name='water')

    def __str__(self):
        return self.title


class Image(models.Model):
    title = models.TextField()
    cover = models.ImageField(upload_to='images/')
    property = models.ForeignKey(
        Property, on_delete=models.CASCADE, related_name="property_images")

    def __str__(self):
        return self.cover.url


class Meeting(models.Model):
    property = models.ForeignKey(
        Property, on_delete=models.CASCADE, related_name="meeting")
    visitor = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="meeting")
    date = models.DateField(blank=False, null=False)
    hour = models.IntegerField(default=9, blank=False, null=False,
                               validators=[MinValueValidator(9), MaxValueValidator(14)])

    class Meta:
        unique_together = ('date', 'hour',)
