from django.contrib import admin
from .models import Post, Category


class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug_url": ("title")}


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug_url": ("name")}


admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
