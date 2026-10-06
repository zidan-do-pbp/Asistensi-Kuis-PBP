from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.http import HttpResponseNotAllowed

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
            response = redirect('main:login')
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