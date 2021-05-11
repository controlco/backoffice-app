from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class User(AbstractUser):
    is_active = models.BooleanField(default=False, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')
    rut = models.CharField(max_length=10, blank=True, null=True)
    birth_date = models.DateTimeField(blank=True, null=True)
    is_owner = models.BooleanField(default=True)
    pass
