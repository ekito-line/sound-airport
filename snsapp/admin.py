from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Post, User, Follow, Like

# Register your models here.
admin.site.register(Post)
admin.site.register(User, UserAdmin)
admin.site.register(Follow)
admin.site.register(Like)