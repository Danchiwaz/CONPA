from unicodedata import name
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views


urlpatterns = [
   path('profile/', views.profile, name="profile"),
   path('register/', views.registerUser, name="register_user"),
   path('accounts/login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name="user_login"),
   path('accounts/logout/', auth_views.LogoutView.as_view(), name="user_logout"),
]