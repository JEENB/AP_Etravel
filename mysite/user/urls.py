from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.userinfo, name='userinfo'),
    path('update-profile/', views.updateprofile, name='updateprofile'),
    path('password/', views.updatepassword, name='updatepassword'),


]

