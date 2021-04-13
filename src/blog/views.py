from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, View
from .forms import PostForm, EditForm
from .models import Post, Category


class NavBarView(View):
    cat_menu = Category.objects.all().only('name')

    def get_context_data(self, *args, **kwargs):
        context = super(NavBarView, self).get_context_data(*args, **kwargs)
        context['cat_menu'] = self.cat_menu
        return context


class HomeView(NavBarView, ListView):
    model = Post
    template_name = 'home.html'
    ordering = ['-post_date']


class ArticleDetailView(NavBarView, DetailView):
    model = Post
    
    def get(self, request, slug):
        article = Post.objects.get(slug_url=slug)
        context = {'post': article, 'cat_menu': self.cat_menu}
        return render(request, 'article_details.html', context)


class CategoryView(NavBarView, ListView):
    model = Category
    template_name = 'categories.html'
    ordering = ['id']


class CategoryDetailView(NavBarView, DetailView):
    model = Post
    slug_field = 'slug_url'
    
    def get(self, request, slug):
        category_name = Category.objects.get(slug_url=slug)
        filtered_posts = Post.objects.filter(category=category_name).order_by('-post_date')
        context = {'filtered_posts': filtered_posts,
                   'category_name': category_name,
                   'cat_menu': self.cat_menu}
        return render(request, 'category_detail.html', context)
