from django.urls import path
from . import views


urlpatterns = [
    path('', views.home_redirect, name='home'),      # root redirect logic
    path('accept/', views.accept, name='accept'),
    path('', views.accept, name='accept'),
    path('<int:id>/', views.resume, name='resume'),
    path('list/', views.list, name='list'),
]
