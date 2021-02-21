from django.urls import path

from posts import views

urlpatterns =[
  path(
    route='', 
    view=views.PostsFeedView.as_view(), 
    name="feed"),
  path(
    route='new/', 
    view=views.NewPostView.as_view(), 
    name='new_post'),
  
  path(
    route='<str:username>/<int:pk>',
    view= views.PostDetailView.as_view(),
    name='details'
  )
]
