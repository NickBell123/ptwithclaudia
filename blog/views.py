from django.shortcuts import render, get_object_or_404, redirect, reverse
from .models import Blog_post
from .forms import BlogPostForm, CategoryBlogForm
# Create your views here.

def blog_posts(request):
    """ A veiw for the blog posts page """
    blog_posts = Blog_post.objects.all().order_by('date_posted').reverse()
    
    context = {
        'blog_posts': blog_posts
    }

    return render(request, 'blog/blog.html', context)


def likes_view(request, pk):
    liked_post = get_object_or_404(Blog_post, id=request.POST.get('blog_post_id'))
    liked_post.likes.add(request.user)

    return redirect (reverse('blog_detail', args=[str(pk)]))


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


def add_category(request):
    if request.method == 'POST':
        form = CategoryBlogForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('blog')
    
    form = CategoryBlogForm
    context = {
        'form': form
    }
    return render(request, 'blog/add_category.html', context)


def category_view(request, name):
    category_posts = Blog_post.objects.filter(category=name)

    context = {
        'name': name,
        'category_posts': category_posts
    }
    return render(request, 'blog/category_view.html', context)


def blog_detail(request, blog_id):
    blog_post = get_object_or_404(Blog_post, pk=blog_id)
    total_likes = blog_post.get_total_likes()
    context = {
        'total_likes': total_likes,
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
    blog_post.delete()
    return redirect('blog')