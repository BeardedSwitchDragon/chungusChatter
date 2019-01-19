from django.urls import path
from chatterApp import views

app_name = "chatterApp"

urlpatterns = [
    path("register", views.register, name="register"),
    path("login", views.user_login, name="user_login"),
    path("logout", views.user_logout, name="logout"),
    path("chat", views.user_chat, name="chat"),
]
