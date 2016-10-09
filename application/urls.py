"""untitled URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from application.views import index, CreatePostsView, ListPostsView, DeletePostsView, UpdatePostsView

urlpatterns = [
    url(r'^test/', index, name="test"),
    url(r'^create/', CreatePostsView.as_view(), name="create_post"),
    url(r'^$', ListPostsView.as_view(), name="list_posts"),
    url(r'^delete/(?P<pk>\d)', DeletePostsView.as_view(), name="delete_posts"),
    url(r'^update/(?P<pk>\d)', UpdatePostsView.as_view(), name="update_posts"),

]


