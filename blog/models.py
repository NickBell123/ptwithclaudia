from django.db import models
from django.contrib.auth.models import User
from datetime import datetime, date
from ckeditor.fields import RichTextField

class Category(models.Model):
    name = models.CharField(max_length=250)
    
    def __str__(self):
        return self.name


class Blog_post(models.Model):
    title = models.CharField(max_length=250)
    author = models.ForeignKey(User, on_delete=models.CASCADE) #Cascade used to remove all posts if user deleted
    category = models.CharField(max_length=250, null=True, blank=True)
    body = RichTextField(blank=True, null=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True, upload_to="blog_post_images/")
    date_posted = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(User, related_name='blog_likes')
    
    def get_total_likes(self):
        return self.likes.count()

    def __str__(self):
        return self.title + ' : ' + str(self.author)

class Comment(models.Model):
    post = models.ForeignKey(Blog_post, related_name="comments", on_delete=models.CASCADE)
    name = models.CharField(max_length=50, null=True, blank=True)
    body = RichTextField(blank=True, null=True)
    date_posted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.post.title + ' : ' + str(self.name)