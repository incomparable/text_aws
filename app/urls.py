"""my_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('Doctor/', views.doctor, name='doctor'),
    path('Patient/', views.patient, name='patient'),
    path('Email/', views.send_email, name='send_email'),
    path('get_doctor/<int:id>/', views.get_doctor, name='get_doctor'),
    path('get_patient/<int:id>/', views.get_patient, name='get_patient'),
    path('update_doctor/', views.update_doctor, name='update_doctor'),
    path('delete-doctor/<int:id>/', views.delete_doctor, name='delete_doctor'),
    path('delete-patient/<int:id>/', views.delete_patient, name='delete_patient'),
]
