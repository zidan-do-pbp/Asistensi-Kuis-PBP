from django.contrib.auth import views as auth_views
from django.urls import path

from main.views import create_project, delete_project, edit_project, project_list, toggle_star

# FILE INI TIDAK DIUBAH SAAT KUIS (sudah jadi). Dibaca supaya tahu nama yang harus dipakai di views.py dan template.
# Cara baca: path("alamat/", fungsi_view, name="nama_url")
#   - "alamat/"   : URL yang diketik di browser / dipakai action form
#   - fungsi_view : fungsi di main/views.py yang dijalankan (harus sama persis dengan nama fungsi dan di-import di atas)
#   - name        : dipakai redirect("main:name") dan {% url 'main:name' %} di template. "main" = app_name di bawah
# <int:project_id> = bagian URL yang ditangkap lalu dikirim ke view sebagai parameter bernama project_id (nama WAJIB sama)

app_name = "main"  # namespace: redirect("main:project_list")

urlpatterns = [
    # GET / -> project_list() (SUDAH JADI): kirim projects, is_owner, is_editor ke project_list.html. Tujuan redirect semua view soal 2
    path("", project_list, name="project_list"),
    # Login/Logout memakai class-based view bawaan Django (tidak perlu ditulis). LoginView render main/login.html. LOGIN_URL di settings = "main:login"
    path("login/", auth_views.LoginView.as_view(template_name="main/login.html"), name="login"),
    path("logout/", auth_views.LogoutView.as_view(next_page="main:project_list"), name="logout"),
    # GET/POST /projects/create/ -> create_project() (urutan 1, Owner only, selain itu 403). Link di template: {% url 'main:create_project' %}
    path("projects/create/", create_project, name="create_project"),
    # /projects/3/edit/ -> edit_project(request, project_id=3) (urutan 2, Owner/Editor). Parameter view WAJIB project_id. Template: {% url 'main:edit_project' project.id %}
    path("projects/<int:project_id>/edit/", edit_project, name="edit_project"),
    # POST /projects/3/delete/ -> delete_project(request, project_id=3) (urutan 3, POST + Owner). GET = 405. Template: form post + csrf_token
    path("projects/<int:project_id>/delete/", delete_project, name="delete_project"),
    # POST /projects/3/star/ -> toggle_star(request, project_id=3) (urutan 4, login + POST). Tambah/hapus user di Project.starred_by
    path("projects/<int:project_id>/star/", toggle_star, name="toggle_star"),
]
