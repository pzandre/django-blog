from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from datetime import datetime, date

class Post(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    preview = models.Charfield(max_length=255)
    body = models.TextField()
    tags = models.CharField(max_length=255)
    post_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title + ' | ' + str(self.author)

    def get_absolute_url(self):
        return reverse('article-detail', args=[str(self.id)])
