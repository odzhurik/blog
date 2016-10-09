# -*- coding: utf-8 -*-
# Create your views here.
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DeleteView, UpdateView
from application.forms import PostForm
from application.models import Post


class FormTitleMixin(object):
    def get_context_data(self, **kwargs):
        context = super(FormTitleMixin,self).get_context_data()
        if self.form_title:
         context['form_title'] = self.form_title
        return context


def index(request):
    return render(request, 'index.html')


class CreatePostsView(FormTitleMixin, CreateView):
    model = Post
    form_class = PostForm
    template_name = 'create.html'
    form_title = u'Create your post'


class ListPostsView(ListView):
    model = Post
    template_name = 'index.html'
    context_object_name = 'posts'


class DeletePostsView(FormTitleMixin,DeleteView):
    model = Post
    template_name = 'create.html'
    success_url = reverse_lazy("app:list_posts")
    form_title = u' are you really delete?'


class UpdatePostsView(FormTitleMixin,UpdateView):
    model = Post
    template_name = 'create.html'
    success_url = reverse_lazy("app:list_posts")
    form_title = u' are you want to update?'
    form_class = PostForm

