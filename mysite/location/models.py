from django.db import models
from hotel.models import Category
from ckeditor_uploader.fields import  RichTextUploadingField
from django.utils.safestring import mark_safe

# Create your models here.
class Locations(models.Model):
    country = models.ForeignKey(Category, on_delete= models.CASCADE)
    AREA = (
        ('Paro', 'Paro'),
        ('Thimpu', 'Thimpu'),
        ('Punakha', 'Punakha'),
        ('Kathmandu', 'Kathmandu'),
        ('Pokhara', 'Pokhara'),
        ('Lumbini', 'Lumbini'),
    )   
    location = models.CharField(max_length=20, choices=AREA, null= True) 
    description = RichTextUploadingField()
    places  = RichTextUploadingField()
    image = models.URLField(default='')



    def image_tag(self):
        if self.image:
            return mark_safe('<img src="{}" height="40"/>'.format(self.image))
        else:
            return " No Image Found"
    image_tag.short_description = 'Image'

class Images(models.Model):
    location              = models.ForeignKey(Locations, on_delete = models.CASCADE)
    image               = models.URLField(default='') 
    image_Description   = models.CharField(max_length = 50)

    def __str__(self):
        return self.image_Description
