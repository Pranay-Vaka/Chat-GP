from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from .models import Forum, Message


def index(request: HttpRequest):
    response = "Thank youuu.... I think that might just be what i need to buuuusssss"
    return HttpResponse(response)


def category_view(request: HttpRequest, category: str):
    allForums = Forum.forums.filter(category=category)
    print(f"{allForums=}")
    return HttpResponse(allForums)


def forum_view(request: HttpRequest, category: str, forum: str):
    allMessages = Message.messages.filter(
        forum__name__contains=forum, forum__category__contains=category
    )
    print(f"{allMessages=}")
    return HttpResponse(allMessages)
