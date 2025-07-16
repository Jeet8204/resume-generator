from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_redirect, name='home'),  # Only one '' route
    path('accept/', views.accept, name='accept'),
    path('resume/<int:id>/', views.download_resume, name='resume'),
    path('list/', views.profile_list, name='list'),
]
