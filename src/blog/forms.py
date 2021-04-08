from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'author', 'body', 'tags']
        
        help_texts = {
            'title': 'Choose a interesting title',
            'body': 'Tell us a nice story',
        }

        widget = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter the title for your post'}),
            'author': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Who are you?'}),
            'body': forms.Textarea(attrs={'class': 'form-control', 'placeholder': "What's in your mind?"}),
            'tags': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'What is this post related to?'}),
        }


class EditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'body', 'tags']

        help_texts = {
            'title': 'Choose a interesting title',
            'body': 'Tell us a nice story',
        }

        widget = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter the title for your post'}),
            'body': forms.Textarea(attrs={'class': 'form-control', 'placeholder': "What's in your mind?"}),
            'tags': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'What is this post related to?'}),
        }