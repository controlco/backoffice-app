from django.db import models
from accounts.models import User
# Create your models here.


class Property(models.Model):
    title = models.TextField()
    owner = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="property")
