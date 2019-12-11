from django.db import models
from django.contrib.auth.models import AbstractUser , User
from crawling.models import Stream
# Create your models here.
class User(AbstractUser):
    nickname = models.CharField(max_length=200)
    favorite = models.ManyToManyField(Stream, related_name="fav_user") 
    