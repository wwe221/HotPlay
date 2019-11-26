from django.db import models

# Create your models here.
class Stream(models.Model):
    channel_name = models.CharField(max_length=50)
    channel_url = models.CharField(max_length=100)
    channel_thumbnail = models.CharField(max_length=100 , null=True)
    title = models.CharField(max_length=50)
    stream_url= models.CharField(max_length=50)
    stream_views = models.IntegerField()
    stream_thumbnail = models.CharField(max_length=100)