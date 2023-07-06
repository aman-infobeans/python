from django.urls import re_path
from AppProfile import views

app_name = "AppProfile"

urlpatterns = [
    re_path(r"^$", views.index, name="index"),
    re_path(r"^logout\/$", views.user_logout, name="logout"),
    re_path(r"^register\/$", views.register, name="register"),
    re_path(r"^login\/$", views.user_login, name="login"),
]
