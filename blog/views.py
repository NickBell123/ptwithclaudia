from django.shortcuts import render
from .models import Blog_post
# Create your views here.

def blog_posts(request):

    """ A veiw for the blog posts page """
    blog_posts = Blog_post.objects.all()

    context = {
        'blog_posts': blog_posts
    }

    return render(request, 'blog/blog.html', context)