from django.db import models
from ckeditor_uploader.fields import  RichTextUploadingField
from django.urls import reverse
from django.utils.safestring import mark_safe
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.db.models import Avg, Count

# Create your models here.

class Category(models.Model):
    COUNTRY = (
        ('Bhutan', 'Bhutan'),
        ('Nepal', 'Nepal'),
    )
    parent = models.ForeignKey('self',blank=True, null=True ,related_name='children', on_delete=models.CASCADE)
    country = models.CharField(max_length=120, choices=COUNTRY)
    description = RichTextUploadingField(null=True)
    
    def __str__(self):
        return self.country

class Hotel(models.Model):
    AREA = (
        ('Paro', 'Paro'),
        ('Thimpu', 'Thimpu'),
        ('Punakha', 'Punakha'),
        ('Kathmandu', 'Kathmandu'),
        ('Pokhara', 'Pokhara'),
        ('Lumbini', 'Lumbini'),
    )
    country     = models.ForeignKey(Category, on_delete= models.CASCADE)
    location    = models.CharField(max_length=120, choices=AREA)
    location_overview   = models.CharField(max_length=250, default = 'Set against the Himalayas, this polished, palatial hotel built to resemble a 17th-century fortress overlooks the Paro River and is 4 km from the airport, and 7 km from Rinpung Dzong, a famed Buddhist monastery/fortress.')
    amenities   = RichTextUploadingField(default= 'hkajsdfh')
    title       = models.CharField(max_length=120)
    description = RichTextUploadingField(null=True)
    image       = models.URLField(default='')
    price       = models.DecimalField(max_digits=1000, decimal_places=2)
    rooms       = models.IntegerField()
    slug        = models.SlugField(unique = True, null = False, max_length=20)

#django aggregation to count reviews and average reviews
    def countrev(self):
        countreview = Review.objects.filter(hotel= self).aggregate(count=Count('id'))
        counter = int(countreview["count"])
        return counter

    def averagerev(self):
        averagereview = Review.objects.filter(hotel= self).aggregate(average=Avg('rate'))
        if averagereview["average"] is None:
            avg = 0
            return avg
        else:
            avg = float(averagereview["average"])
            return avg


    def get_absolute_url(self):
        return reverse('hotel_title', kwargs={'slug': self.slug})

    def image_tag(self):
        if self.image:
            return mark_safe('<img src="{}" height="40"/>'.format(self.image))
        else:
            return " No Image Found"
    image_tag.short_description = 'Image'

class Images(models.Model):
    hotel               = models.ForeignKey(Hotel, on_delete = models.CASCADE)
    image               = models.URLField(default='') 
    image_Description   = models.CharField(max_length = 50)

    def __str__(self):
        return self.hotel.title

class Review(models.Model):
    user    = models.ForeignKey(User, on_delete= models.CASCADE)
    hotel   = models.ForeignKey(Hotel, on_delete= models.CASCADE)
    comment = models.CharField(max_length=1000)
    rate    = models.IntegerField(default=0,)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.hotel.title
        
    @property
    def hotel_name(self):
        return (self.hotel.title)


    
        
class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ['comment', 'rate']