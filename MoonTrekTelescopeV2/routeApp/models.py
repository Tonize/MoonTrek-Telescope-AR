from django.db import models

# Create your models here.

from django.db import models

# Create your models here.

class MoonPost(models.Model):

    #Here we create the fields that our db is gonna contain for every capture(picutre)

    user_image= models.ImageField(upload_to='user_images_raw',blank=False) #this is for the image
    # time= models.TimeField(auto_now=False, auto_now_add=False , blank=False)  #this is for the time
    # longitude = models.DecimalField(max_digits=9, decimal_places=6, blank=False) #this is for longitude
    # latitude = models.DecimalField(max_digits=9, decimal_places=6,blank=False)  #this is for latitude
