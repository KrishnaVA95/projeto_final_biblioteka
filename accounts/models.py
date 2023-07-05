from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class Accounts(models.Model):
    nome = models.CharField(max_length=127)
    email = models.EmailField(max_length=127, unique=True)
    password = models.CharField(max_length=127)
    is_staff = models.BooleanField(default=False)
    address = models.CharField(max_length=255)
    created_at = models.DateField(auto_now_add=True)
    permission_loan = models.BooleanField(default=False)
