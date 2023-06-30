from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Account(AbstractUser):
    is_staff = models.BooleanField(default=False)
    cpf = models.IntegerField()
    created_at = models.DateField(auto_now_add=True)
    