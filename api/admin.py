from django.contrib import admin
from .models import Post, Comment


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'created_at', 'is_published']
    list_filter = ['is_published', 'created_at', 'author']
    search_fields = ['title', 'content']
    date_hierarchy = 'created_at'
    list_editable = ['is_published']


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['author_name', 'post', 'created_at']
    list_filter = ['created_at', 'post']
    search_fields = ['author_name', 'content']
    date_hierarchy = 'created_at'
