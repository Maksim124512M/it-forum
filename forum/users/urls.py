from django.urls import path
from django.contrib.auth import views as auth
from . import views

urlpatterns = [
    path('login/', auth.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('signup/', views.UserSignupView.as_view(), name='signup'),
    path('profile/', views.ProfileView.as_view(), name='profile'),
]