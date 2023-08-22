from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, View
from .forms import PostForm, EditForm
from .models import Post, Category


def home(request):
    return render(request, 'home.html')


class ArticleDetailView(DetailView):
    model = Post
    
    def get(self, request, slug):
        article = Post.objects.get(slug_url=slug)
        context = {'post': article, 'cat_menu': self.cat_menu}
        return render(request, 'article_details.html', context)


class CategoryView(ListView):
    model = Category
    template_name = 'categories.html'
    ordering = ['id']


class CategoryDetailView(DetailView):
    model = Post
    slug_field = 'slug_url'
    
    def get(self, request, slug):
        category_name = Category.objects.get(slug_url=slug)
        filtered_posts = Post.objects.filter(category=category_name).order_by('-post_date')
        context = {'filtered_posts': filtered_posts,
                   'category_name': category_name,
                   'cat_menu': self.cat_menu}
        return render(request, 'category_detail.html', context)
