# Generated by Django 3.1.3 on 2020-11-28 16:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog_post',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='blog_post',
            name='image_url',
            field=models.URLField(blank=True, max_length=1024, null=True),
        ),
    ]
