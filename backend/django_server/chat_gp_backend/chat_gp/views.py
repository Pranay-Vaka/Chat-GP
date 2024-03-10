from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.core import serializers
from django.contrib.auth.models import User
from .models import Category, Forum, Message, Post


def index(request: HttpRequest):
    response = b"Thank youuu.... I think that might just be what i need to buuuusssss"
    return HttpResponse(response, content_type="text/plain")


def category_all(request: HttpRequest):
    allCategories = Category.categories.all()
    data = serializers.serialize("json", allCategories)
    return HttpResponse(data, content_type="application/json")


def category_view(request: HttpRequest, category: str):
    allForums = Forum.forums.filter(category__name__contains=category)
    data = serializers.serialize("json", allForums)
    print(f"{data=}")
    return HttpResponse(data, content_type="application/json")


def forum_view(request: HttpRequest, category: str, forum: str):
    category_obj = Category.categories.get(name=category)
    forum_obj = Forum.forums.get(name=forum, category=category_obj)
    data = serializers.serialize("json", [forum_obj])
    print(f"{data=}")
    return HttpResponse(data, content_type="application/json")


def forum_messages(request: HttpRequest, category: str, forum: str):
    category_obj = Category.categories.get(name=category)
    forum_obj = Forum.forums.get(name=forum, category=category_obj)
    allMessages = Message.messages.filter(forum=forum_obj)
    data = serializers.serialize("json", allMessages)
    print(f"{data=}")
    return HttpResponse(data, content_type="application/json")


def forum_posts(request: HttpRequest, category: str, forum: str):
    allPosts = Post.posts.select_related("user", "forum").filter(
        forum__name=forum, forum__category__name=category
    )
    data = serializers.serialize("json", allPosts)
    print(f"BUSSSS {data=}")
    return HttpResponse(data, content_type="application/json")
