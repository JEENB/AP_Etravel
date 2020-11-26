from django.db import models
from ckeditor_uploader.fields import  RichTextUploadingField
from django.urls import reverse

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
    title       = models.CharField(max_length=120)
    description = RichTextUploadingField(null=True)
    image       = models.URLField(default='')
    price       = models.DecimalField(max_digits=1000, decimal_places=2)
    rooms       = models.IntegerField()
    slug        = models.SlugField(unique = True, null = False, max_length=20)

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
