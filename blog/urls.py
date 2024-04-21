from django.urls import path
from . import views

urlpatterns = [
    path('', views.getHome, name='post_list'),
    path('post/new/', views.createPost, name='post_new'),
]