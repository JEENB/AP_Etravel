from django.urls import path
from . import views

urlpatterns = [
    path('wishlistcart/<int:id>/', views.addtowishlist, name= 'addtowishlist'),
    path('wishlistremove/<int:id>/', views.wishlistremove, name= 'wishlistremove'),



]
