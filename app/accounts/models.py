from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse
# Create your models here.


class User(AbstractUser):
    is_active = models.BooleanField(default=False, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
        blank=False,
        null=False,
        )
    rut = models.CharField(max_length=10, blank=True, null=True)
    birth_date = models.DateTimeField(blank=True, null=True)
    is_owner = models.BooleanField(default=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    
    
    def get_absolute_url(self):
        return reverse('user-detail', args=[str(self.id)])
    
    def __str__(self):
        return self.email
    
