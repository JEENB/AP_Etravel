from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from .forms import Signup, UserUpdate, ProfileCreate
from user.models import Profile
from django.contrib.auth.forms import PasswordChangeForm


# Create your views here.

def signout_page(request):
    logout(request)
    return HttpResponseRedirect('/')


def loginform(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user     = authenticate(request, username= username, password=password)
        if user is None:
            messages.warning(request,"Username or Password incorrect!!")  
            return HttpResponseRedirect('/login')
        else:
            login(request, user)
            return HttpResponseRedirect('/')
    context ={}
    return  render (request, "login.html", context)


def signupform(request):
    if request.method == 'POST':
        form = Signup(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user     = authenticate(username= username, password= password)
            login(request, user)
            

            # saving sign up info to Profile
            current_user = request.user
            user         = Profile()
            user.user_id = current_user.id
            user.save()
            return HttpResponseRedirect('/')
        else: 
            messages.warning(request,form.errors)
            return HttpResponseRedirect('/signup')

    form = Signup()
    
    context ={'form': form,}
    return  render (request, "signup.html", context)


@login_required(login_url = '/login')
def userinfo(request):
    current_user = request.user
    prof         = Profile.objects.get(user_id = current_user.id)
    context      = {
        'prof': prof
    }
    return render(request, 'userprofile.html', context) 

#profile update requires userupdate and profile update
@login_required(login_url = '/login')
def updateprofile(request):
    if request.method == 'POST':
        userupdate_form = UserUpdate(request.POST, instance= request.user)
        profileupdate_form = ProfileCreate(request.POST, instance= request.user.profile)
        if profileupdate_form.is_valid() and userupdate_form.is_valid():
            profileupdate_form.save()
            userupdate_form.save()
            messages.success(request,'Your profile has been updated!!')
            return HttpResponseRedirect('/user')
        else: 
            messages.error(request,'Error! Please check your credentials')
            return HttpResponseRedirect('/user/update-profile')


    userupdate_form = UserUpdate(instance= request.user)
    profileupdate_form = ProfileCreate(instance= request.user.profile)
    context ={
        'userupdate_form': userupdate_form,
        'profileupdate_form': profileupdate_form
    }
    return render(request, 'userupdate.html', context)

@login_required(login_url = '/login')
def updatepassword(request):
    if request.method == 'POST':
        password_form = PasswordChangeForm(request.user, request.POST)
        if password_form.is_valid():
            user = password_form.save()
            update_session_auth_hash(request, user)
            messages.success(request,'Your password has been updated!!')
            return HttpResponseRedirect('/')
        else:
            messages.error(request, password_form.errors)
            return HttpResponseRedirect('/user/password')

    password_form = PasswordChangeForm(request.user)
    context = {
        'password_form': password_form
    }
    return render (request, 'passwordupdate.html', context)