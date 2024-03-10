from django.contrib import admin
from .models import Forum, Message, Category, Post

# Register your models here.
admin.site.register(Post)
admin.site.register(Forum)
admin.site.register(Message)
admin.site.register(Category)
