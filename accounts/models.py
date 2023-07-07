from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class Account(AbstractUser):
    username = models.CharField(max_length=127)
    password = models.CharField(max_length=127)
    cpf = models.CharField(max_length=11, null=False, unique=True)
    email = models.EmailField(max_length=127, unique=True)
    is_staff = models.BooleanField(default=False)
    address = models.CharField(max_length=255)
    created_at = models.DateField(auto_now_add=True)
    permission_loan = models.BooleanField(default=False)
