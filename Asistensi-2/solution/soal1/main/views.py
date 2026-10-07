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


# ALUR SOAL 1: hanya ubah main/views.py (urls, template, settings JANGAN disentuh)
# Urutan kerja: register -> login_user -> logout_user
# Import yang dipakai sudah ada di atas: login, logout, forms bawaan, HttpResponseNotAllowed, timezone


# HUBUNGAN: urls.py path("register/", register, name="register") -> fungsi ini. Template main/register.html membaca konteks {{ form }}
# HUBUNGAN: redirect("main:login") = app_name "main" + name "login" di urls.py (urls.py tidak diubah)
# TODO: (urutan 1) register. Kontrak soal 1 poin 1
def register(request):
    # TODO: (urutan 1a) POST: isi UserCreationForm dari request.POST
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        # TODO: (urutan 1b) POST valid: simpan User lalu redirect ke named route main:login
        if form.is_valid():
            form.save()
            return redirect("main:login")
        # POST tidak valid: tidak ada User dibuat, jatuh ke render di bawah (form + error)
    else:
        # TODO: (urutan 1c) GET: form kosong
        form = UserCreationForm()
    return render(request, "main/register.html", {"form": form})


# HUBUNGAN: urls.py name="login" -> fungsi ini. login.html membaca {{ form }}. Cookie last_login dibaca home() lewat request.COOKIES.get("last_login") lalu dikirim ke home.html sebagai {{ last_login }}
# TODO: (urutan 2) login_user. Kontrak soal 1 poin 2
def login_user(request):
    if request.method == "POST":
        # TODO: (urutan 2a) AuthenticationForm WAJIB menerima request sebagai argumen pertama
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            # TODO: (urutan 2b) panggil login() dengan user dari form.get_user()
            login(request, form.get_user())
            # TODO: (urutan 2c) buat response redirect dulu, baru pasang cookie di response itu
            response = redirect("main:home")
            # TODO: (urutan 2d) cookie last_login format %Y-%m-%d %H:%M:%S, tanpa password atau username
            # BONUS: max_age=3600, httponly=True, samesite="Lax"
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


# HUBUNGAN: tombol Logout di home.html adalah <form method="post"> + {% csrf_token %} ke {% url 'main:logout' %}; link GET harus 405, makanya cek POST di sini
# TODO: (urutan 3) logout_user. Kontrak soal 1 poin 3
def logout_user(request):
    # TODO: (urutan 3a) selain POST: HTTP 405 (kunci: "POST" pakai kutip, bandingkan dengan request.method)
    if request.method != "POST":
        return HttpResponseNotAllowed(["POST"])
    # TODO: (urutan 3b) logout(), redirect ke main:home, hapus cookie last_login di response
    logout(request)
    response = redirect("main:home")
    response.delete_cookie("last_login")
    return response
