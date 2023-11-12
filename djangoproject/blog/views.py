from multiprocessing import AuthenticationError
from telnetlib import AUTHENTICATION
from django.shortcuts import render



# from djangoproject.djangoproject.settings import AUTH_PASSWORD_VALIDATORS


from . models import *
# Create your views here.
from django.shortcuts import render
from . import urls
# Create your views here.
def loadindex(request):
    #displaying from table
    obj1=Cake.objects.all()  #to display 
    obj2=latestposts.objects.all()


    return render(request,'index.html',{'data':obj1,'data1':obj2})#to pass data here data is a key word we choose any name
def loadsinglepost(request):
    obj1=singleposts.objects.all()
    return render(request,'single_post.html',{'data','obj1'})
