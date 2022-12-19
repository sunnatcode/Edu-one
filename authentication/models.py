from statistics import mode
from django.db import models
from django.db.models import CASCADE
from django.contrib.auth.models import User
# Create your models here.


class Register(models.Model):
    user = models.OneToOneField(User, on_delete=CASCADE, null=True)
    phone = models.IntegerField()
