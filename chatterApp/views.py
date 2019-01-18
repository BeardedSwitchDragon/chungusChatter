from django.shortcuts import render
from chatterApp.forms import ChatterUserForm, ChatterUserProfileForm

from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login, logout
logged_in = False
# Create your views here.
def index(request):
    if logged_in:
        print(User.objects.filter(username=username))
        return render(request, "chatterApp/user_login.html")#, {"profile_pic": user_profile_pic})
    else:
        return render(request, "chatterApp/user_login.html")


@login_required
def user_logout(request):
    return HttpResponseRedirect(reverse("index"))


def user_chat(request):
    return render(request, "chatterApp/chat.html")

def register(request):
    registered = False

    if request.method == "POST":
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request)

        if user_form.is_valid() and profile_form.is_valid():

            user = user_form.save()
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
        user_form = ChatterUserForm()
        profile_form = ChatterUserProfileForm()

    return render(request, "chatterApp/register.html", {"user_form": user_form,
                                                            "profile_form": profile_form,
                                                            "registered": registered})


def user_login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse("index"))
            else:
                return HttpResponse("sorry borry account ain't active")
        else:
            print("login faillllllled")
            print("username: {0} and password {1}".format(username, password))

    else:
        logged_in = True
        return render(request, "basic_app/login.html", {})
