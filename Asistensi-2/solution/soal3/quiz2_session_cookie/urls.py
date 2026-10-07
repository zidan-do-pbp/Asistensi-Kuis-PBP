"""
URL configuration for quiz2_session_cookie project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path

# DOKUMENTASI (file ini jangan diubah): path('', include('main.urls')) = semua URL di main/urls.py dipasang di root (alamat kosong).
# Makanya /login/ di main/urls.py jadi http://127.0.0.1:8000/login/. 'admin/' = halaman admin Django. Awalan 'main:' dari app_name di main/urls.py.
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
]
