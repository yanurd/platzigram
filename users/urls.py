from django.urls import path

from users import views

urlpatterns = [
  
  path(
    route='login/',
    view=views.Login.as_view(),
    name="login"
  ),
  path(
    route='logout/',
    view=views.LogOut.as_view(),
    name='logout'
  ),

  path(
    route='signup/',
    view=views.SignUp.as_view(),
    name='signup'
  ),

  path(
    route='me/profile/',
    view=views.UpdateProfile.as_view(),
    name='update_profile'
  ),
  path(
    route='<str:username>/',
    view= views.UserDetailView.as_view(),
    name='user_detail',
  ),
    
]