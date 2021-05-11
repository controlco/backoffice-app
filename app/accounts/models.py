from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class User(AbstractUser):
    pass


class Report(models.Model):
    title = models.CharField(max_length=50, default="Report")
    content = models.TextField()
    owner = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="from_report")
    reported_user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="to_report")
