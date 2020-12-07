# Generated by Django 3.1.3 on 2020-12-07 10:29

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0005_auto_20201206_1142'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog_post',
            name='likes',
            field=models.ManyToManyField(related_name='blog_likes', to=settings.AUTH_USER_MODEL),
        ),
    ]
