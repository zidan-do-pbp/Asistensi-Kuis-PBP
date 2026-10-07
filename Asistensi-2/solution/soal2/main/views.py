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


@login_required
def create_project(request):
    if not is_owner(request.user):
        raise PermissionDenied
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


@login_required
def edit_project(request, project_id):
    if not (is_owner(request.user) or is_editor(request.user)):
        raise PermissionDenied
    project = get_object_or_404(Project, pk=project_id)
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


@login_required
@require_POST
def delete_project(request, project_id):
    if not is_owner(request.user):
        raise PermissionDenied
    project = get_object_or_404(Project, pk=project_id)
    project.delete()
    return redirect("main:project_list")


@login_required
@require_POST
def toggle_star(request, project_id):
    project = get_object_or_404(Project, pk=project_id)
    if project.starred_by.filter(pk=request.user.pk).exists():
        project.starred_by.remove(request.user)
    else:
        project.starred_by.add(request.user)
    return redirect("main:project_list")
