from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from .models import WishlistCart
from django.contrib.auth.decorators import login_required


@login_required(login_url = '/login')
def addtowishlist(request,id):
    get_url = request.META.get('HTTP_REFERER')
    current_user = request.user 

    hotel = WishlistCart.objects.filter(hotel_id = id)
    if hotel:
        wishlist_obj = WishlistCart.objects.get(hotel_id = id)
        wishlist_obj.save
    else:
        wishlist_obj = WishlistCart()
        wishlist_obj.user_id = current_user.id
        wishlist_obj.hotel_id = id
        wishlist_obj.save()
    messages.success(request, "Hotel added to Wishlist")
    return HttpResponseRedirect(get_url)


@login_required(login_url = '/login')
def wishlist(request):
    current_user = request.user
    wishlists = WishlistCart.objects.filter(user_id = current_user.id)

    context = { 
        'wishlists'  : wishlists,

    }
    return render(request, 'wishlist.html', context)

@login_required(login_url = '/login')
def wishlistremove(request, id):
    WishlistCart.objects.filter(id = id).delete()
    context = {

    }
    return HttpResponseRedirect("/wishlist")