"""
URL configuration for resume_generator project.

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
from django.urls import path, include
from pdf import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home_redirect, name="home"),       # Root URL → login or /accept
    path('accept/', views.accept, name="accept"),      # Resume form
    path('resume/<int:id>/', views.download_resume, name='resume'),
    path('list/', views.profile_list, name="list"),
    path('accounts/', include('allauth.urls')),        # Google login + auth
]
