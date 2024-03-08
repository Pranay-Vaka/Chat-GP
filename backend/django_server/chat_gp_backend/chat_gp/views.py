from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.core import serializers
from .models import Category, Forum, Message


def index(request: HttpRequest):
    response = "Thank youuu.... I think that might just be what i need to buuuusssss"
    return HttpResponse(response)


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
    allMessages = Message.messages.filter(
        forum__name__contains=forum, forum__category__contains=category
    )
    data = serializers.serialize("json", allMessages)
    print(f"{data=}")
    return HttpResponse(data, content_type="application/json")
