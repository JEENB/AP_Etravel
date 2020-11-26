from django.shortcuts import render
from django.http import HttpResponse
from hotel.models import Hotel, Category
# Create your views here.

def home_page_view(request):
    return HttpResponse("my home page")


def about_page_view(request):
    return HttpResponse("my about page")

def contact_page_view(request):
    return HttpResponse("my contact page")

def terms_page_view(request):
    return HttpResponse("my terms page")    

def destination_nepal(request):
    return HttpResponse("nepal")

def destination_bhutan(request):
    return HttpResponse("bhutan")