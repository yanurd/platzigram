from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from django.views.generic import ListView, DetailView, CreateView
#Models
from posts.models import Post

#Forms
from posts.forms import PostForm

class PostsFeedView(LoginRequiredMixin, ListView):
  template_name = 'posts/feed.html'
  model = Post
  ordering = ('-created',)
  paginate_by = 2
  context_object_name = 'posts'

class PostDetailView(LoginRequiredMixin, DetailView):
  template_name = 'posts/detail.html'
  queryset = Post.objects.all()
  context_object_name = 'posts'
  
class NewPostView(LoginRequiredMixin, CreateView):
  form_class = PostForm
  template_name = 'posts/new.html'
  success_url = reverse_lazy('posts:feed')

  ##Como debo enviar el usuario y perfil al contexto
  ##sobreescribo la clase get_context_data

  def get_context_data(self, **kwargs):
      context = super().get_context_data(**kwargs)
      context["user"] = self.request.user
      context['profile'] = self.request.user.profile
      return context
  