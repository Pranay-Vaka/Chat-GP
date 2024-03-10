from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("category/all", views.category_all, name="category-all"),
    path("<str:category>/forums", views.category_view, name="category"),
    path("<str:category>/<str:forum>/", views.forum_view, name="forum"),
    path("<str:category>/<str:forum>/messages", views.forum_messages, name="messages"),
    path("<str:category>/<str:forum>/posts", views.forum_posts, name="forum-posts"),
]
