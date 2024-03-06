from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<str:category>/forums', views.category_view, name='category'),
    path('<str:category>/<str:forum>/posts', views.forum_view, name='forum'),
]
