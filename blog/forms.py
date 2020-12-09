from django import forms
from .models import Blog_post, Category, Comment

categories = Category.objects.all().values_list('name', 'name')
category_list = []

for item in categories:
    category_list.append(item)

class CategoryBlogForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),  
        }

class BlogPostForm(forms.ModelForm):
    class Meta:
        model = Blog_post
        fields = ['title', 'author', 'category', 'body', 'image_url', 'image']

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'author': forms.Select(attrs={'class': 'form-control'}),
            'category': forms.Select(choices=category_list, attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
            'image_url': forms.TextInput(attrs={'class': 'form-control'}),   
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'body']

        widgets = {
            
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),

        }