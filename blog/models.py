from django.db import models
from django.contrib.auth.models import User
from datetime import datetime, date

class Category(models.Model):
    name = models.CharField(max_length=250)
    
    def __str__(self):
        return self.name


class Blog_post(models.Model):
    title = models.CharField(max_length=250)
    author = models.ForeignKey(User, on_delete=models.CASCADE) #Cascade used to remove all posts if user deleted
    category = models.CharField(max_length=250, null=True, blank=True)
    body = models.TextField()
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    date_posted = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(User, related_name='blog_likes')
    
    def get_total_likes(self):
        return self.likes.count()

    def __str__(self):
        return self.title + ' : ' + str(self.author)