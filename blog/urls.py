from django.urls import path
from . import views

urlpatterns = [
    path('', views.getHome, name='post_list'),
]