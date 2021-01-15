from django.contrib import admin
from .models import Post, Comment

# Register your models here.

class PostAdmin(admin.ModelAdmin):
    """
    Class for registering model Post on admin page
    """
    fields = ['title', 'link']


class CommentAdmin(admin.ModelAdmin):
    """
    Class for registering model Comment on admin page
    """
    fields = ['comment']


admin.site.register(Post, PostAdmin)

admin.site.register(Comment, CommentAdmin)