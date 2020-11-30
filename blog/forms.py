from django import forms
from .models import Blog_post


class BlogPostForm(forms.ModelForm):
    class Meta:
        model = Blog_post
        fields = ['title', 'author', 'body', 'image_url', 'image']

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'author': forms.Select(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
            'image_url': forms.TextInput(attrs={'class': 'form-control'}),
            
        }