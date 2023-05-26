from django.contrib import admin
from .models import Comment, User, Post, Likes
# Register your models here.

admin.site.register(Comment)

admin.site.register(User)

#admin.site.register(Likes)
@admin.register(Likes)
class LikesAdmin(admin.ModelAdmin):
    list_display = ('pos', 'user_like')

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('user', 'id', 'date')
