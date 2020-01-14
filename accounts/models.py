from django.db import models
from django.contrib.auth.models import AbstractUser , User
from crawling.models import Stream
import random
# Create your models here.
class User(AbstractUser):
    nickname = models.CharField(max_length=200)
    favorite = models.ManyToManyField(Stream, related_name="fav_user") 
    
    def randstr(self,length):
        rstr = "0123456789abcdefghijklnmopqrstuvwxyzABCDEFGHIJKLNMOPQRSTUVWXYZ"
        rstr_len = len(rstr) - 1
        result = ""
        for i in range(length):
            result += rstr[random.randint(0, rstr_len)]
        return result