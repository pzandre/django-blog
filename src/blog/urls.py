from django.urls import path
from .views import HomeView, ArticleDetailView, AddPostView, UpdatePostView, \
                   DeletePostView, CategoryView, CategoryDetailView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('article/<slug:slug>', ArticleDetailView.as_view(), name='article-detail'),
    path('add_post/', AddPostView.as_view(), name='add-post'),
    path('article/edit/<int:pk>', UpdatePostView.as_view(), name='update-post'),
    path('article/<int:pk>/delete', DeletePostView.as_view(), name='delete-post'),
    path('categories/', CategoryView.as_view(), name='categories'),
    path('categories/<slug:slug>', CategoryDetailView.as_view(), name='category-detail'),
]
