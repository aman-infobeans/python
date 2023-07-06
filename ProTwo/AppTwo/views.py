from django.shortcuts import render
from django.http import HttpResponse
from . import forms
from AppTwo.models import Topic, Chapter, Users
from AppTwo.forms import UserForm

# Create your views here.


def index(req):
    return HttpResponse("<em>I am Speed</em>")


def help(req):
    chapter = Chapter.objects.order_by("chaptername")
    dict = {"chapters": chapter}
    return render(req, "AppTwo/help.html", dict)


def users(req):
    form = UserForm()

    if req.method == "POST":
        form = UserForm(req.POST)
        if form.is_valid():
            form.save(commit=True)
            return index(req)
        else:
            print("sad")

    user_list = Users.objects.order_by("Firstname")
    dict = {"users": user_list, "form": form}
    return render(req, "AppTwo/users.html", dict)
