from django.db import models

# Create your models here.
from django.db import models
from hotel.models import Hotel
from django.contrib.auth.models import User
from django.forms import ModelForm

# Create your models here.


class WishlistCart(models.Model):
    user        = models.ForeignKey(User, on_delete=models.SET_NULL, null= True)
    hotel     = models.ForeignKey(Hotel, on_delete=models.SET_NULL, null= True)
    created     = models.DateTimeField(auto_now_add=True)
    updated     = models.DateTimeField(auto_now=True)

    @property
    def prod(self):
        return (self.hotel.title)
 

    @property
    def price(self):
        return (self.hotel.price)