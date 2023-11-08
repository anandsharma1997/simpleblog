from django.contrib import admin
from .models import Post, Category, HomeContent, Comment
# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display=['id','title','title_tag', 'author','categary', 'body', 'header_image']

admin.site.register(Post, PostAdmin)

class CategoryAdmin(admin.ModelAdmin):
    list_display=['id','name']

admin.site.register(Category, CategoryAdmin)

class HomeContentAdmin(admin.ModelAdmin):
    list_display = ['id', 'blog_heading', 'blog_heading_body']

admin.site.register(HomeContent, HomeContentAdmin)


class CommentAdmin(admin.ModelAdmin):
    list_display = ['id', 'post', 'name', 'body', 'date_dated']

admin.site.register(Comment, CommentAdmin)