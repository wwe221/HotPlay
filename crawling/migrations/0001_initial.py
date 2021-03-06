# Generated by Django 2.2.7 on 2019-12-12 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Stream',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('channel_name', models.CharField(max_length=50)),
                ('channel_url', models.CharField(max_length=100, null=True)),
                ('channel_thumbnail', models.CharField(max_length=100, null=True)),
                ('title', models.CharField(max_length=50)),
                ('stream_url', models.CharField(max_length=50)),
                ('stream_embed_url', models.CharField(max_length=50)),
                ('stream_views', models.IntegerField()),
                ('stream_thumbnail', models.CharField(max_length=100)),
                ('tof', models.IntegerField(null=True)),
                ('platform', models.IntegerField()),
                ('on_air', models.IntegerField()),
            ],
        ),
    ]
