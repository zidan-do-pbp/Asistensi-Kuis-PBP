from django.contrib.auth import views as auth_views
from django.urls import path

from main.views import dashboard, dismiss_announcement, reset_preferences, set_theme

# FILE INI TIDAK DIUBAH SAAT KUIS (sudah jadi). Dibaca supaya tahu nama yang harus dipakai di views.py dan template.
# Cara baca: path("alamat/", fungsi_view, name="nama_url")
#   - "alamat/"   : URL yang diketik di browser / dipakai action form
#   - fungsi_view : fungsi di main/views.py yang dijalankan (harus sama persis dengan nama fungsi dan di-import di atas)
#   - name        : dipakai redirect("main:name") dan {% url 'main:name' %} di template. "main" = app_name di bawah
# 
app_name = "main"  # namespace: redirect("main:dashboard")

urlpatterns = [
    # GET / -> dashboard() (urutan 1, @login_required). Belum login -> redirect ke LOGIN_URL "main:login" + ?next=/. Template: dashboard.html
    path("", dashboard, name="dashboard"),
    # Login/Logout pakai class-based view bawaan Django. Logout next_page="main:login" (setelah logout ke halaman login)
    path("login/", auth_views.LoginView.as_view(template_name="main/login.html"), name="login"),
    path("logout/", auth_views.LogoutView.as_view(next_page="main:login"), name="logout"),
    # POST /preferences/theme/ -> set_theme() (urutan 2): terima field "theme" (light/dark) dari tombol di dashboard.html, simpan di SESSION, lainnya 400
    path("preferences/theme/", set_theme, name="set_theme"),
    # POST /announcement/dismiss/ -> dismiss_announcement() (urutan 3): set COOKIE announcement_dismissed=1 (7 hari). Dibaca dashboard()
    path("announcement/dismiss/", dismiss_announcement, name="dismiss_announcement"),
    # POST /preferences/reset/ -> reset_preferences() (urutan 4): pop theme + visit_count dari session, hapus cookie. User tetap login
    path("preferences/reset/", reset_preferences, name="reset_preferences"),
]
