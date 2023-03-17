from django.urls import path
from authapp import views
from django.contrib.auth.views import LogoutView
from authapp.apps import AuthappConfig

app_name = AuthappConfig.name

urlpatterns = [
    path("register/", views.RegiserView.as_view(), name="register"),
    path("login/", views.CustomLoginView.as_view(), name="login"),
    path("profile/<int:pk>", views.ProfileView.as_view(), name="profile"),
    path("users/", views.UsersView.as_view(), name="users"),
    path("logout/", LogoutView.as_view(), name="logout"),
]
