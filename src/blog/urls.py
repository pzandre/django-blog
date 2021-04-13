from django.urls import path
from .views import HomeView, ArticleDetailView, DeletePostView, CategoryView, CategoryDetailView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('article/<slug:slug>', ArticleDetailView.as_view(), name='article-detail'),
    path('article/<slug:slug>/delete', DeletePostView.as_view(), name='delete-post'),
    path('categories/', CategoryView.as_view(), name='categories'),
    path('categories/<slug:slug>', CategoryDetailView.as_view(), name='category-detail'),
]
