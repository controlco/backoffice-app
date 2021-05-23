from django.db import models
from accounts.models import User
# Create your models here.


class Message(models.Model):
    subject = models.CharField(max_length=100, default="[Sin Asunto]")
    content = models.TextField(blank=False, null=False)
    from_user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="from_message")
    to_user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="to_message")
    date_time = models.DateTimeField(auto_now_add=True)
    read = models.BooleanField(default=False)
