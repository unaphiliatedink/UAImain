"""UAImain URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')

"""
from django.urls import path
from . import views # For function based views
from .views import documentsIndex, consent_form, success

urlpatterns = [
    path('', documentsIndex.as_view(), name='documents_index'),
    path('consent_form/', consent_form, name='consent_form'),
    path('success/', success, name='success'),
]
