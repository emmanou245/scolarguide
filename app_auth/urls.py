from django.urls import path

from guide.views import dashbordAdm
from .views import loginGuide, logoutGuide, log0Guide

urlpatterns = [
    path('authenfication', log0Guide, name='log0Guide'),
    path('login', loginGuide, name='loginGuide'),
    path('accueil/', logoutGuide, name="logoutGuide")
]