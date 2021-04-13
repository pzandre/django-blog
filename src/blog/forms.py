from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'author', 'preview', 'body', 'slug_url', 'tags', 'category']
        
        help_texts = {
            'preview': '255 chars max',
            'slug_url': "If you don't know what you're doing, leave it   as it is",
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Enter the title for your post'})
        self.fields['author'].widget.attrs.update({'class': 'form-control'})
        self.fields['preview'].widget.attrs.update({'class': 'form-control', 'placeholder': 'This will show at the Home Page'})
        self.fields['body'].widget.attrs.update({'class': 'form-control', 'placeholder': 'What is in your mind?'})
        self.fields['tags'].widget.attrs.update({'class': 'form-control','placeholder': 'What is this post related to?'})
        self.fields['category'].widget.attrs.update({'class': 'form-control'})
        self.fields['slug_url'].widget.attrs.update({'class': 'form-control', 'placeholder': 'The post URL'})


class EditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'preview', 'body', 'tags', 'category']

        help_texts = {
            'preview': '255 chars max',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Enter the title for your post'})
        self.fields['preview'].widget.attrs.update({'class': 'form-control', 'placeholder': 'This will show at the Home Page'})
        self.fields['body'].widget.attrs.update({'class': 'form-control', 'placeholder': "What's in your mind?"})
        self.fields['tags'].widget.attrs.update({'class': 'form-control','placeholder': 'What is this post related to?'})
        self.fields['category'].widget.attrs.update({'class': 'form-control'})



