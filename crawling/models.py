from django.db import models

# Create your models here.
class Stream(models.Model):
    # id =  models.AutoField(auto_created=True,serialize=False, verbose_name='ID', primary_key=True)
    channel_name = models.CharField(max_length=50)
    channel_url = models.CharField(max_length=100, null=True)
    channel_thumbnail = models.CharField(max_length=100 , null=True)
    title = models.CharField(max_length=50)
    stream_url= models.CharField(max_length=50)
    stream_embed_url= models.CharField(max_length=50)
    stream_views = models.IntegerField()
    stream_thumbnail = models.CharField(max_length=100)
    tof = models.IntegerField(null=True)
    platform = models.IntegerField()
    on_air = models.IntegerField()