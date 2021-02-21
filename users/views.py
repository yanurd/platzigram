from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User

#Generic Views
from django.views.generic import DetailView, FormView, UpdateView
from django.contrib.auth.views import LogoutView, LoginView
#Exceptions
from django.db.utils import IntegrityError

#Models
from users.models import Profile
from posts.models import Post
#Forms
from users.forms import SignupForm
# Create your views here.

class UpdateProfile(LoginRequiredMixin, UpdateView):
  template_name = 'users/update_profile.html'
  model = Profile
  fields = ['biography','picture','website','phone_number']

  def get_object(self):
    ##return user's profile
    return self.request.user.profile
  
  def get_success_url(self):
    ##return to users profile
    username = self.object.user.username
    return reverse('users:user_detail', kwargs={'username': username})

class Login(LoginView):
  template_name = 'users/login.html'
  redirect_authenticated_user = True
  success_url = '/'

class SignUp(FormView):
  form_class = SignupForm
  template_name = 'users/signup.html'
  success_url = reverse_lazy('users:login')

  def form_valid(self, form):
    form.save()
    return super().form_valid(form)

class LogOut(LoginRequiredMixin, LogoutView):
  ##Logs out user
  template_name = 'users/login.html'

##Ir a un user específico
class UserDetailView(LoginRequiredMixin, DetailView):
  template_name = 'users/detail.html'
  slug_field = 'username'  #Es lo que busco en BBDD
  slug_url_kwarg = 'username' ##parametro que envio en urls <str:username>
  queryset = User.objects.all()
  context_object_name = 'user'

  def get_context_data(self, **kwargs):
      context = super().get_context_data(**kwargs)
      user = self.get_object()
      context["posts"] =  Post.objects.filter(user=user).order_by('-created')
      return context
  