"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page_view, name='home_page_view'),
    path('home/', views.home_page_view, name='home_page_view'),
    path('aboutus/', views.about_page_view, name='about_page_view'),
    path('contact/', views.contact_page_view, name='contact_page_view'),
    path('terms/', views.terms_page_view, name='terms_page_view'),
    path('destination/nepal/', views.destination_nepal, name='destination_nepal'),
    path('destination/bhutan/', views.destination_bhutan, name='destination_bhutan'),
    path('search/', views.search_page_view, name='search_page_view'),
    path('search_ajax/', views.search_ajax, name='search_ajax'),
    path('hotel/<int:id>/<slug:slug>/', views.hotel_detail_view, name='hotel_detail_view'),

]
