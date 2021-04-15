from ckeditor.fields import RichTextField
from colorfield.fields import ColorField
from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from datetime import datetime, date


class Category(models.Model):
    class Meta:
        verbose_name_plural = "categories"

    name = models.CharField(max_length=255)
    slug_url = models.SlugField(max_length=50)
    navbar_color = ColorField(default='#343A40')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('home')


class Post(models.Model):
    title = models.CharField(max_length=255)
    slug_url = models.SlugField(max_length=50)
    header_image = models.ImageField(null=True, blank=True, upload_to="header_images/")
    header_img_alt_text = models.CharField(max_length=255, null=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    preview = models.CharField(max_length=255)
    body = RichTextField(blank=True, null=True)
    tags = models.CharField(max_length=255)
    post_date = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.title + ' | ' + str(self.author)

    def get_absolute_url(self):
        return reverse('home')
