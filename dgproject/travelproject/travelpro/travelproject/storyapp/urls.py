from . import views
from django.urls import path
from django.contrib import admin
urlpatterns = [
    path('register', views.register, name='register'),
    path('login', views.login, name="login"),
    path('logout', views.logout, name="logout"),
]
