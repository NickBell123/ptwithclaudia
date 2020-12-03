from django.shortcuts import render, get_object_or_404, redirect
from .models import Blog_post
from .forms import BlogPostForm
# Create your views here.

def blog_posts(request):

    """ A veiw for the blog posts page """
    blog_posts = Blog_post.objects.all()
    context = {
        'blog_posts': blog_posts
    }

    return render(request, 'blog/blog.html', context)

def add_post(request):
    if request.method == 'POST':
        form = BlogPostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('blog')
    
    form = BlogPostForm
    context = {
        'form': form
    }
    return render(request, 'blog/add_blog_post.html', context)


def blog_detail(request, blog_id):
    blog_post = get_object_or_404(Blog_post, pk=blog_id)
    context = {
        'blog_post': blog_post
    }

    """A view to see single blog details"""
   
    return render(request, 'blog/blog_detail.html', context)


def edit_blog(request, blog_id):
    blog_post = get_object_or_404(Blog_post, pk=blog_id)
    if request.method == 'POST':
        form = BlogPostForm(request.POST, instance=blog_post)
        if form.is_valid():
            form.save()
            return redirect('blog')
    
    form = BlogPostForm(instance=blog_post)
    context = {
        'form': form
    }

    """A view to see single blog details"""
   
    return render(request, 'blog/edit_blog.html', context)


def delete_blog(request, blog_id):
    blog_post = get_object_or_404(Blog_post, pk=blog_id)
    if request.method == 'POST':
        blog_posts.delete()
        return redirect('blog')