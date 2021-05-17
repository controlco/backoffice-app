from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.urls import reverse
# Create your models here.


class UserManager(BaseUserManager):

    def create_user(self, email, password, is_superuser=False, first_name=None, last_name=None, rut=None, birth_date=None, is_active=False, is_owner=False):

        if is_superuser:
            user = self.model(
                email=self.normalize_email(email)
            )
        else:
            if not all([email, first_name, last_name, password]):
                raise ValueError(
                    'Users Must Have an email, password, first name and last name.')
            user = self.model(
                email=self.normalize_email(email),
                is_owner=is_owner,
                first_name=first_name,
                last_name=last_name,
                rut=rut,
                birth_date=birth_date,
                is_active=is_active
            )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):

        if password is None:
            raise TypeError('Superusers must have a password.')

        user = self.create_user(
            email=email, password=password, is_superuser=True)
        user.is_superuser = True
        user.is_staff = True
        user.is_active = True
        user.save(using=self._db)

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


class Report(models.Model):
    title = models.CharField(max_length=100, default="Report")
    content = models.TextField()
    owner = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="from_report")
    reported_user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="to_report")
