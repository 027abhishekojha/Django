from django.contrib import admin

from blog.models import Post, Comment


# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'created_at', 'modified_at']

admin.site.register(Post, PostAdmin)


class CommentAdmin(admin.ModelAdmin):
    list_display = ['post', 'text', 'created_at', 'modified_at']
admin.site.register(Comment, CommentAdmin)