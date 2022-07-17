from distutils.command.upload import upload
from django.db import models
# model ==> class working with DB

class Project(models.Model):
        # find Django model field documentation
        title = models.CharField(max_length=100)
        discription = models.CharField(max_length=250)
        image = models.ImageField(upload_to='portfolio/images/') #name of folder that I want to store images
        url = models.URLField(blank=True) #Some projects are clickable but some are not

