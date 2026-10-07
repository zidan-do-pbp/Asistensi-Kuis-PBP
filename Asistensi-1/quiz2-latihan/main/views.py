from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.http import HttpResponseNotAllowed, HttpResponseForbidden
from .models import Project
from .forms import ProjectForm

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('main:login')
    else:
        form = UserCreationForm()
    return render(request, 'main/register.html', {'form': form})

def login_user(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            response = redirect('main:create_project')
            response.set_cookie('last_login', 'placeholder')
            return response
    else:
        form = AuthenticationForm()
    return render (request, 'main/login.html', {'form': form})

def logout_user(request):
    if request.method == 'POST':
        logout(request)
        response = redirect('main:login') 
        response.delete_cookie('last_login')
        return response
    return HttpResponseNotAllowed(['POST'])

def project_list(request):
    projects = Project.objects.all()
    return render(request, 'main/projects.html', {'projects': projects})

def create_project(request):
    if not request.user.groups.filter(name='Owner').exists():
        return HttpResponseForbidden()
    form = ProjectForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('main:project_list')
    return render(request, 'main/projects_form.html', {"form": form})

def edit_project(request, project_id):
    if not request.user.groups.filter(name__in=['Owner', 'Editor']).exists():
        return HttpResponseForbidden()
    project = get_object_or_404(Project, pk=project_id)
    form = ProjectForm(request.POST or None, instance=project)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('main:project_list')
    return render(request, 'main/projects_form.html', {"form":form})