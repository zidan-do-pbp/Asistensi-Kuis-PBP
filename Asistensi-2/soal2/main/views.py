from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_POST

from main.forms import ProjectForm
from main.models import Project


def has_role(user, role_name):
    return user.groups.filter(name=role_name).exists()

def is_editor(user):
    return has_role(user, "Editor")

def is_owner(user):
    return has_role(user, "Owner")

# HUBUNGAN: is_editor / is_owner di konteks ini = variabel yang dibaca project_list.html ({% if is_owner %}), BUKAN user.is_owner
def project_list(request):
    projects = Project.objects.prefetch_related("starred_by").all()
    return render(
        request,
        "main/project_list.html",
        {
            "projects": projects,
            "is_editor": has_role(request.user, "Editor"),
            "is_owner": has_role(request.user, "Owner"),
        },
    )


# ALUR SOAL 2: ubah main/views.py (urutan 1 sampai 4) lalu templates/main/project_list.html (urutan 5)
# Cek role SELALU di server memakai is_owner/is_editor yang sudah ada. Dilarang is_superuser.
# Urutan kerja views: create_project -> edit_project -> delete_project -> toggle_star


# HUBUNGAN: urls.py "projects/create/" name="create_project" -> fungsi ini. Template project_form.html membaca {{ form }} dan {{ heading }}. Link-nya dipasang di project_list.html (urutan 5A) pakai {% url 'main:create_project' %}
# TODO: (urutan 1) create_project. Hanya Owner, selain itu PermissionDenied (HTTP 403)
@login_required
def create_project(request):
    # TODO: (urutan 1a) cek Owner dulu sebelum memproses apa pun
    if not is_owner(request.user):
        raise PermissionDenied
    # TODO: (urutan 1b) POST: ProjectForm(request.POST), valid -> save lalu redirect main:project_list
    if request.method == "POST":
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("main:project_list")
    else:
        form = ProjectForm()
    return render(
        request,
        "main/project_form.html",
        {"form": form, "heading": "Tambah Project"},
    )


# HUBUNGAN: urls.py "projects/<int:project_id>/edit/" -> parameter view WAJIB bernama project_id (sama persis). Di template: {% url 'main:edit_project' project.id %}
# TODO: (urutan 2) edit_project. Hanya Editor atau Owner. User biasa 403
@login_required
def edit_project(request, project_id):
    if not (is_owner(request.user) or is_editor(request.user)):
        raise PermissionDenied
    # TODO: (urutan 2a) ambil objek dengan get_object_or_404 (id tidak ada -> 404). Nama parameter harus project_id (sama dengan urls.py)
    project = get_object_or_404(Project, pk=project_id)
    # TODO: (urutan 2b) pakai instance=project agar form meng-update, bukan membuat baru
    if request.method == "POST":
        form = ProjectForm(request.POST, instance=project)
        if form.is_valid():
            form.save()
            return redirect("main:project_list")
    else:
        form = ProjectForm(instance=project)
    return render(
        request,
        "main/project_form.html",
        {"form": form, "heading": "Edit Project"},
    )


# HUBUNGAN: urls.py "projects/<int:project_id>/delete/" -> project_id. Template: <form method="post"> + csrf_token ke {% url 'main:delete_project' project.id %}; link GET = 405 karena require_POST
# TODO: (urutan 3) delete_project. Hanya POST (require_POST sudah ada) dan hanya Owner
@login_required
@require_POST
def delete_project(request, project_id):
    if not is_owner(request.user):
        raise PermissionDenied
    # TODO: (urutan 3a) hapus objek lalu redirect ke daftar
    project = get_object_or_404(Project, pk=project_id)
    project.delete()
    return redirect("main:project_list")


# HUBUNGAN: urls.py "projects/<int:project_id>/star/" -> project_id. Model Project.starred_by (ManyToMany ke User) dihitung di template: {{ project.starred_by.count }}
# TODO: (urutan 4) toggle_star. POST + login. Sudah ada di starred_by -> hapus, belum -> tambah
# BONUS: prefetch_related("starred_by") sudah dipakai di project_list
@login_required
@require_POST
def toggle_star(request, project_id):
    project = get_object_or_404(Project, pk=project_id)
    if project.starred_by.filter(pk=request.user.pk).exists():
        project.starred_by.remove(request.user)
    else:
        project.starred_by.add(request.user)
    return redirect("main:project_list")
