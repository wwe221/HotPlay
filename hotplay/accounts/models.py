from django.db import models
from django.contrib.auth.models import AbstractUser , User
# Create your models here.
class User(AbstractUser):
    address = models.CharField(max_length=200)
    