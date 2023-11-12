from django.db import models

# Create your models here.
from django.db import models

class Cake(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    
    image = models.ImageField(upload_to='cakes/', null=True, blank=True)
    date= models.DateField(auto_now_add=True)
    mt=models.CharField(max_length=100)
    
    author=models.CharField(max_length=100,default="author name")
class latestposts(models.Model):
    image = models.ImageField(upload_to='latestposts/', null=True,blank=True)
    title=models.DateField(auto_now_add=True)
    date=models.DateField(auto_now_add=True)
    
class singleposts(models.Model):
    image = models.ImageField(upload_to='singleposts/', null=True,blank=True)
    name=models.CharField()
    author=models.CharField()
    
   