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
from django.urls import path, include
from home import urls
from user import urls
from hotel import urls
from user import views as userviews
from hotel import views as hotelviews
from destination import views as wishlistviews
from location import views as locationviews
from django.conf.urls import url
urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', include('home.urls')),
    path('', include('home.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('signout/', userviews.signout_page, name= 'signout'),
    path('login/', userviews.loginform, name= 'loginform'),
    path('signup/', userviews.signupform, name= 'signupform'),
    path('user/', include('user.urls')),
    path('hotel/', include('hotel.urls')),
    path('billing/', hotelviews.billing, name='billing'),
    path('accounts/', include('allauth.urls')),
    path('wishlist/', include('destination.urls')),
    path('wishlist/', wishlistviews.wishlist, name= 'wishlist'),
    path('location/<int:id>', locationviews.location, name= 'location'),


]
