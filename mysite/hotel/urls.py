from django.urls import path, include
from . import views

urlpatterns = [
    path('addreview/<int:id>', views.addreview, name='addreview'),
    path('booking/<int:id>/', views.book_hotel, name='book_hotel'),

]