from django.shortcuts import render
from AppProfile.forms import UserProfileForm, Userform

from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required

# Create your views here.


def index(request):
    return render(request, "AppProfile/index.html")


def user_login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse("AppProfile:index"))
            else:
                return HttpResponse("User is not active")
        else:
            return HttpResponse("Login Failed")
    else:
        return render(request, "AppProfile/login.html")


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse("AppProfile:login"))


def register(request):
    registered = False

    if request.method == "POST":
        user_form = Userform(request.POST)
        profile_form = UserProfileForm(request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save(commit=True)
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            if "profile_pic" in request.FILES:
                profile.profile_pic = request.FILES["profile_pic"]

            profile.save()

            registered = True
        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form = Userform()
        profile_form = UserProfileForm()

    data = {
        "UserForm": user_form,
        "UserProfileForm": profile_form,
        "registered": registered,
    }

    return render(request, "AppProfile/register.html", data)
