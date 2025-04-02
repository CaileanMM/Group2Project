"""
URL configuration for UNCCtutor project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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

# from django.contrib import admin
from django.urls import path
from django.contrib import admin
from django.http import HttpResponse
from django.shortcuts import render
from . import views

urlpatterns = [
       # path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('login/', views.loginPage, name="login"),
    path('register/', views.registerPage, name='register'),
    path('profile/', views.userProfile, name='user-profile'),
    path('edit-profile/', views.editProfile, name='edit-profile'),
    path('edit-classes/', views.editClasses, name='edit-classes'),
    path('tutor-finder/', views.tutorFinder, name='tutor-finder'),
    path('tutor-profile/', views.tutorProfile, name='tutor-profile'),
    path('support/', views.support, name='support'),
]

