from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from hotel.models import Hotel, Category, Images, Review
from .forms import Search
import json
from django.core.paginator import Paginator
from complaints.models import Complaint, ComplaintForm
from django.contrib import messages
from location.models import Locations
from hotel.filters import HotelFilter
from django.db.models import Q


# Create your views here.

def home_page_view(request):
    hotels = Hotel.objects.all().order_by('?')[:8]
    loc = Locations.objects.all().order_by('?')[:8]
    context ={
        'hotels': hotels,
        'loc':  loc
    }
    return render(request, 'home.html', context)


def search_page_view(request):
    if request.method == "POST":
        form = Search(request.POST)
        if form.is_valid():
            query           = form.cleaned_data['query']
            lookup = Q(title__icontains=query) | Q(location__icontains=query) 

            search_hotel    = Hotel.objects.filter(lookup)
            
            
            context={
                'search_hotel': search_hotel,
                'query': query
                    }
            return render(request, 'search.html', context)


#====================================================================
#auto search; copied from http://www.lalicode.com/post/5/ #citation
def search_ajax(request):
  if request.is_ajax():
    q = request.GET.get('term', '')
    hotels = Hotel.objects.filter(title__icontains=q)
    results = []
    for smart in hotels:
      hotel_json = {}
      hotel_json = smart.title 
      results.append(hotel_json)
    data = json.dumps(results)
  else:
    data = 'fail'
  mimetype = 'application/json'
  return HttpResponse(data, mimetype)  
#====================================================================

def about_page_view(request):
    context ={}
    return render(request, 'about.html', context)


def contact_page_view(request):
    if request.method =='POST':
        form = ComplaintForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Thank you for contacting us!')
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        else:
            messages.error(request,'Error! Please check your credentials')
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))   

    form = ComplaintForm()         
            
    context ={'form': form} 
    return render(request, 'contact.html', context)


def terms_page_view(request):
    context ={}
    return render(request, 'terms.html', context)


def hotel_detail_view(request, id, slug):
    hotel      = Hotel.objects.get(pk = id)
    img         = Images.objects.filter(hotel_id= id)
    more_like   = Hotel.objects.all().order_by('?')[:4]
    reviews     = Review.objects.filter(hotel_id = id).order_by('?')[:4]
    context     = {
        'hotel'   : hotel,
        'more_like' : more_like,
        'img'       : img,
        'reviews'   : reviews
    }
    return render(request, 'hotel_detail.html', context)

def destination_nepal(request):
    hotels = Hotel.objects.filter(country=2)[:]
    hotel_filter = HotelFilter(request.GET, queryset = hotels)

    paginator       = Paginator(hotel_filter.qs,9)
    page            = request.GET.get('page')
    hotels          = paginator.get_page(page)
    context = {
        'hotels': hotels,
        'filter': hotel_filter

    }
    return render(request,'nepal.html',context)

def destination_bhutan(request):
    hotels = Hotel.objects.filter(country=1)[:]
    hotel_filter = HotelFilter(request.GET, queryset = hotels)
    

    paginator       = Paginator(hotel_filter.qs,9)
    page            = request.GET.get('page')
    hotels          = paginator.get_page(page)
    
    
    context = {
        'hotels': hotels,
        'filter': hotel_filter
    }
    return render(request,'bhutan.html',context)