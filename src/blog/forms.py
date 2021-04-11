from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'author', 'preview', 'body', 'slug_url', 'tags', 'category']
        
        help_texts = {
            'title': 'Choose a interesting title',
            'body': 'Tell us a nice story',
            'preview': '255 chars max',
            'slug_url': "If you don't know what you're doing, leave as it is",
        }

        widget = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter the title for your post'}),
            'author': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Who are you?'}),
            'body': forms.Textarea(attrs={'class': 'form-control', 'placeholder': "What's in your mind?"}),
            'tags': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'What is this post related to?'}),
            'category': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Choose a category'}),
            'slug_url': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'The post URL'}),
        }


class EditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'preview', 'body', 'tags', 'category']

        help_texts = {
            'title': 'Choose a interesting title',
            'body': 'Tell us a nice story',
            'preview': '255 chars max',
        }

        widget = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter the title for your post'}),
            'body': forms.Textarea(attrs={'class': 'form-control', 'placeholder': "What's in your mind?"}),
            'tags': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'What is this post related to?'}),
            'category': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Choose a category'}),
        }
