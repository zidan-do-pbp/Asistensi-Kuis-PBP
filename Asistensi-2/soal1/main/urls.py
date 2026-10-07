from django.urls import path

from main.views import home, login_user, logout_user, register

# FILE INI TIDAK DIUBAH SAAT KUIS (sudah jadi). Dibaca supaya tahu nama yang harus dipakai di views.py dan template.
# Cara baca: path("alamat/", fungsi_view, name="nama_url")
#   - "alamat/"   : URL yang diketik di browser / dipakai action form
#   - fungsi_view : fungsi di main/views.py yang dijalankan (harus sama persis dengan nama fungsi dan di-import di atas)
#   - name        : dipakai redirect("main:name") dan {% url 'main:name' %} di template. "main" = app_name di bawah
# 
app_name = "main"  # namespace: makanya redirect("main:login"), bukan redirect("login")

urlpatterns = [
    # GET /  -> home(): baca cookie last_login, render home.html. Tujuan redirect setelah login dan logout (main:home)
    path("", home, name="home"),
    # GET/POST /register/ -> register() (soal 1 poin 1). Sukses -> redirect main:login. Template: register.html
    path("register/", register, name="register"),
    # GET/POST /login/ -> login_user() (poin 2). Menulis cookie last_login. Nama "login" juga = LOGIN_URL di settings.py. Template: login.html
    path("login/", login_user, name="login"),
    # /logout/ -> logout_user() (poin 3). POST saja, GET = 405. Tombol logout di home.html harus <form method="post"> + csrf_token
    path("logout/", logout_user, name="logout"),
]
