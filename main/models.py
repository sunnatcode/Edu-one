
from turtle import ondrag
from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User
# Create your models here.


class Auditable(models.Model):
    created_at = models.DateTimeField(default=now)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='+')
    updated_at = models.DateTimeField(default=None, null=True)
    update_by = models.ForeignKey(User, on_delete=models.CASCADE)
    deleted = models.BooleanField(default=False)