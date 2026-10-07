from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.http import HttpResponseNotAllowed
from django.shortcuts import redirect, render
from django.utils import timezone


def home(request):
    return render(
        request,
        "main/home.html",
        {"last_login": request.COOKIES.get("last_login")},
    )


def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("main:login")
    else:
        form = UserCreationForm()
    return render(request, "main/register.html", {"form": form})


def login_user(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            response = redirect("main:home")
            response.set_cookie(
                "last_login",
                timezone.localtime().strftime("%Y-%m-%d %H:%M:%S"),
                max_age=3600,
                httponly=True,
                samesite="Lax",
            )
            return response
    else:
        form = AuthenticationForm()
    return render(request, "main/login.html", {"form": form})


def logout_user(request):
    if request.method != "POST":
        return HttpResponseNotAllowed(["POST"])
    logout(request)
    response = redirect("main:home")
    response.delete_cookie("last_login")
    return response
