from django.urls import re_path
from AppTwo import views

urlpatterns = [
    re_path(r"^help\/$", views.help, name="Help"),
    re_path(r"^users\/$", views.users, name="Users"),
]
