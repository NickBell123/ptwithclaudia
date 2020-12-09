from django.contrib import admin
from .models import Blog_post, Category, Comment

admin.site.register(Blog_post)
admin.site.register(Category)
admin.site.register(Comment)