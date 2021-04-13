from django.urls import path
from .views import HomeView, ArticleDetailView, CategoryView, CategoryDetailView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('article/<slug:slug>', ArticleDetailView.as_view(), name='article-detail'),
    path('categories/', CategoryView.as_view(), name='categories'),
    path('categories/<slug:slug>', CategoryDetailView.as_view(), name='category-detail'),
]
