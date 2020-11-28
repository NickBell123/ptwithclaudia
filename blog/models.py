from django.db import models
from django.contrib.auth.models import User

class Blog_post(models.Model):
    title = models.CharField(max_length=250)
    author = models.ForeignKey(User, on_delete=models.CASCADE) #Cascade used to remove all posts if user deleted
    body = models.TextField()

    def __str__(self):
        return self.title + ' : ' + str(self.author)