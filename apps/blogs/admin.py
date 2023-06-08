from django.contrib import admin

from .models import AuthorBlog, CategoryBlog, Blog, ReviewBlog


@admin.register(AuthorBlog)
class AuthorBlogAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(CategoryBlog)
class CategoryBlogAdmin(admin.ModelAdmin):
    list_display = ['title']


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title", )}
    list_display = ['title', 'author']


@admin.register(ReviewBlog)
class ReviewBlogAdmin(admin.ModelAdmin):
    list_display = ['name', 'blog']
    