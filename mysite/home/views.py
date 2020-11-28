from django.shortcuts import render
from django.http import HttpResponse
from hotel.models import Hotel, Category, Images
from .forms import Search
import json
# Create your views here.

def home_page_view(request):
    hotels = Hotel.objects.all().order_by('?')[:8]
    context ={
        'hotels': hotels
    }
    return render(request, 'home.html', context)


def search_page_view(request):
    if request.method == "POST":
        form = Search(request.POST)
        if form.is_valid():
            query          = form.cleaned_data['query']
            search_hotel = Hotel.objects.filter(title__icontains=query)
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
      hotel_json = smart.title + ", " + smart.location
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
    context ={}
    return render(request, 'contact.html', context)


def terms_page_view(request):
    context ={}
    return render(request, 'terms.html', context)


def hotel_detail_view(request, id, slug):
    hotel      = Hotel.objects.get(pk = id)
    img         = Images.objects.filter(hotel_id= id)
    more_like   = Hotel.objects.all().order_by('?')[:4]
    # reviews     = Review.objects.filter(product_id = id).order_by('?')[:4]
    context     = {
        'hotel'   : hotel,
        'more_like' : more_like,
        'img'       : img,
        # 'reviews'   : reviews
    }
    return render(request, 'hotel_detail.html', context)

def destination_nepal(request):
    hotels = Hotel.objects.filter(country=2).order_by('?')[:]
    context = {
        'hotels': hotels
    }
    return render(request,'nepal.html',context)

def destination_bhutan(request):
    hotels = Hotel.objects.filter(country=1).order_by('?')[:]
    context = {'hotels': hotels}
    return render(request,'bhutan.html',context)