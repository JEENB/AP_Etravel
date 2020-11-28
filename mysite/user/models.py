from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    user        = models.OneToOneField(User, on_delete=models.CASCADE)
    contact     = models.DecimalField(max_digits=10, decimal_places=0, null = True)
    pincode     = models.DecimalField(max_digits=6, decimal_places=0,null = True)
    address     = models.CharField(max_length=150,null = True)
    city        = models.CharField(max_length=50,null = True)
    state       = models.CharField(max_length=50, null = True)
    country     = models.CharField(max_length=50,null = True, default = 'India')
    created     = models.DateTimeField(auto_now_add=True)
    updated     = models.DateTimeField(auto_now=True)


    def name(self):
        return self.user.first_name + ' ' + self.user.last_name + '(' + self.user.username +')'

    def __str__(self):
        return self.user.username