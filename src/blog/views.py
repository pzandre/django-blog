from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .forms import PostForm, EditForm
from .models import Post, Category


class HomeView(ListView):
    model = Post
    template_name = 'home.html'
    ordering = ['-post_date']


class ArticleDetailView(DetailView):
    model = Post
    template_name = 'article_details.html'
    

class AddPostView(CreateView):
    model = Post
    template_name = 'add_post.html'
    form_class = PostForm


class UpdatePostView(UpdateView):
    model = Post
    form_class = EditForm
    template_name = 'update_post.html'


class DeletePostView(DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home')


class CategoryView(ListView):
    model = Category
    template_name = 'categories.html'
    ordering = ['id']


class CategoryDetailView(DetailView):
    model = Post
    template_name = 'category_detail.html'

    def get(self, request, pk, *args, **kwargs):
        filtered_posts = Post.objects.filter(category=pk).order_by('-post_date')
        context = {'filtered_posts': filtered_posts}
        return render(request, 'category_detail.html', context)


