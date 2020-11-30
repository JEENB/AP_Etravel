from django.shortcuts import render
from django.http import HttpResponse
from location.models import Locations, Images
# Create your views here.
def location(request, id):
    loc         = Locations.objects.get(pk = id)
    img         = Images.objects.filter(location_id= id).order_by('?')[:]
    # more_like   = Hotel.objects.all().order_by('?')[:4]
    context     = {
        'loc'   : loc,
        # 'more_like' : more_like,
        'img'       : img,
    }
    return render(request, 'locations.html', context)
