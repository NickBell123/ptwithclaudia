from django.urls import path
from . import views

urlpatterns = [
    path('', views.blog_posts, name='blog'),
    path('add', views.add_post, name='add'),
    path('blog_detail/<int:blog_id>', views.blog_detail, name='blog_detail'),
    path('edit_blog/<int:blog_id>', views.edit_blog, name='edit_blog'),
    path('delete_blog/<int:blog_id>', views.delete_blog, name='delete'),
]
