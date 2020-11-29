from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from hotel.models import Review, ReviewForm, Booking, BookingForm
# Create your views here.


def addreview(request, id):
    current_user = request.user 

    if request.method == 'POST':
        reviewform = ReviewForm(request.POST)
        if reviewform.is_valid():
            rev             = Review()
            rev.comment     = reviewform.cleaned_data['comment']
            rev.rate        = reviewform.cleaned_data['rate']
            rev.user_id     = current_user.id 
            rev.hotel_id  = id
            rev.save()
            messages.success(request, "Your review has been sent. Thank You!!")
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        else:
            messages.error(request, "Error")
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


    return HttpResponseRedirect(geturl)

def book_hotel(request, id):
    current_user = request.user 
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            book                = Booking()
            book.check_in       = form.cleaned_data['check_in']
            book.check_out      = form.cleaned_data['check_out']
            book.guest          = form.cleaned_data['guest']
            book.user_id        = current_user.id 
            book.hotel_id       = id
            book.save()


            return HttpResponseRedirect('/billing/')
        else:
            messages.error(request, "Error")
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))