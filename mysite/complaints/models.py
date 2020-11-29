from django.db import models
from django.forms import ModelForm
from django.forms import TextInput, EmailInput, NumberInput

# Create your models here.
class Complaint(models.Model):
    name = models.CharField(max_length=120, null= True)
    email = models.EmailField()
    complaint = models.CharField(max_length=1000, null = True)
    contact = models.IntegerField()
    booking_code = models.CharField(max_length=14, null= True, blank=True)
    STATUS   = (
        ('New', 'New'),
        ('Resolved', 'Resolved'),
        ('In Process', 'In Process'),
    )
    status = models.CharField(max_length=120, choices=STATUS, default='New')
    note = models.CharField(max_length=500, null= True, blank= True)

    def __str__(self):
        return self.name

class ComplaintForm(ModelForm):
    class Meta:
        model = Complaint
        fields = ( 'name','email', 'complaint', 'contact', 'booking_code')
        widgets = { 
                    'name'          : TextInput(attrs={'placeholder': 'Name'}),
                    'email'         : EmailInput(attrs={'placeholder': 'Email'}),
                    'complaint'    : TextInput(attrs={'placeholder': 'Complaint/ Review'}),
                    'contact'     : NumberInput(attrs={'placeholder': 'Contact'}),   
                    'booking_code'     : TextInput(attrs={'placeholder': 'Booking Code if any'}),   

        }