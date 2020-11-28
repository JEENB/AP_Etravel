from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from django.forms import TextInput, EmailInput, NumberInput
from django.contrib.auth.models import User
from user.models import Profile

class Signup(UserCreationForm):
    username     = forms.CharField(max_length=50, label='Username')
    email        = forms.EmailField(label='Email')
    first_name   = forms.CharField(max_length=50, label='First Name')
    last_name    = forms.CharField(max_length=50, label='Last Name')

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'password1', 'password2')

#user update form for updating signup details
class UserUpdate(UserChangeForm):
    class Meta:
        model = User
        fields = ( 'username','email', 'first_name', 'last_name')
        widgets = { 
                    'username'      : TextInput(attrs={'placeholder': 'username'}),
                    'email'         : EmailInput(attrs={'placeholder': 'email'}),
                    'first_name'    : TextInput(attrs={'placeholder': 'first_name'}),
                    'last_name'     : TextInput(attrs={'placeholder': 'last_name'}),    
        }

#profile form for creating user profile

class ProfileCreate(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('contact', 'pincode', 'address', 'city', 'state','country')
        widgets = {
                    'contact'    : NumberInput(attrs={'placeholder': 'Contact(must be 10 digits)'}),
                    'pincode'    : NumberInput(attrs={'placeholder': 'Pincode(must be 6 digits)'}),
                    'address'    : TextInput(attrs={'placeholder': 'Address'}),
                    'city'       : TextInput(attrs={'placeholder': 'City'}),
                    'state'      : TextInput(attrs={'placeholder': 'State'}),
                    'country'    : TextInput(attrs={'placeholder': 'Country'}),
        }