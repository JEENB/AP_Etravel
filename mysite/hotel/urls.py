from django.urls import path, include
from . import views

urlpatterns = [
    path('addreview/<int:id>', views.addreview, name='addreview'),

]