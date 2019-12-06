from django.db import models

# Create your models here.
class Stream(models.Model):
    id =  models.AutoField(auto_created=True,serialize=False, verbose_name='ID', primary_key=True)
    channel_name = models.CharField(max_length=300)
    channel_url = models.CharField(max_length=300, null=True)
    channel_thumbnail = models.CharField(max_length=300 , null=True)
    title = models.CharField(max_length=300)
    stream_url= models.CharField(max_length=300)
    stream_embed_url= models.CharField(max_length=300)
    stream_views = models.IntegerField()
    stream_thumbnail = models.CharField(max_length=300)
    tof = models.IntegerField(null=True)
    platform = models.IntegerField()