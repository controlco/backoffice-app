from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.urls import reverse
# Create your models here.

class UserManager(BaseUserManager):

    def create_user(self, email, password=None):

        if not email:
            raise ValueError('Users Must Have an email address')

        user = self.model(
            email=self.normalize_email(email),
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):

        if password is None:
            raise TypeError('Superusers must have a password.')

        user = self.create_user(email, password)
        user.is_superuser = True
        user.is_staff = True
        user.is_active = True
        user.save()

        return user


class User(AbstractUser):
    is_active = models.BooleanField(
        default=False, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True)
    username = None
    rut = models.CharField(max_length=10, blank=True, null=True)
    birth_date = models.DateTimeField(blank=True, null=True)
    is_owner = models.BooleanField(default=True)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    
    objects = UserManager() 
    
    def get_absolute_url(self):
        return reverse('user-detail', args=[str(self.id)])

    def __str__(self):
        return self.email

class UserProfile(models.Model):
    id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='profile')
    first_name = models.CharField(max_length=50, unique=False)
    last_name = models.CharField(max_length=50, unique=False)
    rut = models.CharField(max_length=10, blank=True, null=True)
    birth_date = models.DateTimeField(blank=True, null=True)

class Report(models.Model):
    title = models.CharField(max_length=50, default="Report")
    content = models.TextField()
    owner = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="from_report")
    reported_user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="to_report")
