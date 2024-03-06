from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request: HttpRequest):
    response = "Thank youuu.... I think that might just be what i need to buuuusssss"
    return HttpResponse(response)

def category_view(request: HttpRequest, category: str):
    response = f"{category=}"
    return HttpResponse(response)

def forum_view(request: HttpRequest, category: str, forum: str):
    response = f"{category=}, {forum=}"
    return HttpResponse(response)
