from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from hotel.models import Review, ReviewForm, Booking, BookingForm, BookingInfo, BookingInfoForm
from user.models import Profile
from django.utils.crypto import get_random_string
from hotel.models import Hotel
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

def billing(request):
    current_user    = request.user
    billing_form    = BookingInfoForm()
    booking         = Booking.objects.get(user_id = current_user.id)
    profile         = Profile.objects.get(user_id = current_user.id)

    if request.method == 'POST':
        billing_form = BookingInfoForm(request.POST)
        if billing_form.is_valid():
            billing_info               = BookingInfo()
            billing_info.first_name    = billing_form.cleaned_data['first_name']
            billing_info.last_name     = billing_form.cleaned_data['last_name']
            billing_info.email         = billing_form.cleaned_data['email']
            billing_info.contact       = billing_form.cleaned_data['contact']
            billing_info.address       = billing_form.cleaned_data['address']
            billing_info.guest         = billing_form.cleaned_data['guest']
            billing_info.guest_name    = billing_form.cleaned_data['guest_name']
            billing_info.check_in      = billing_form.cleaned_data['check_in']
            billing_info.check_out     = billing_form.cleaned_data['check_out']
            billing_info.total         = billing_form.cleaned_data['total']
            billing_info.cname         = billing_form.cleaned_data['cname']
            billing_info.ccnum         = billing_form.cleaned_data['ccnum']
            billing_info.expmonth      = billing_form.cleaned_data['expmonth']
            billing_info.expyear       = billing_form.cleaned_data['expyear']
            billing_info.cvv           = billing_form.cleaned_data['cvv']
            billing_info.user_id       = current_user.id
            billing_info.hotel         = billing_form.cleaned_data['hotel']

            code                       = get_random_string(length=14)
            billing_info.bookingcode     = code 
            billing_info.save()
            
            Booking.objects.filter(user_id = current_user.id).delete()



                # product = Product.objects.get(id= orders.product_id) 
                # product.quantity -= orders.quantity                        # decreases the quantity of item from database after completion
                # product.save()

            messages.success(request, "Your Booking has been placed. Thank you!!")
            context = { 
                'code'      : code,
            }
            return render(request, 'ordercomplete.html', context)
        else: 
            messages.warning(request, billing_form.errors)
            return HttpResponseRedirect("/billing")
    
    context = {
        'booking'       : booking,
        'profile'       : profile
    }
    return render(request, 'billing.html', context)