from django.shortcuts import redirect, render
from requests import post

from django.contrib.auth.models import User,auth
from django.contrib import messages
# Create your views here.

def loadregister(request):
    if request.method =="POST":
        fn=request.POST["fname"]
        ln=request.POST["lname"]
        email=request.POST["email"]
        uname=request.POST["username"]
        pwd=request.POST["password"]
        cpwd=request.POST["cpassword"]

        if pwd==cpwd:
            if User.objects.filter(username=uname).exists():
                messages.info(request,"username already exist")
                return redirect("loadregister")
            elif User.objects.filter(email=email).exists():
                messages.info(request,"username already exist")
                return redirect("loadregister")
            else:
                res=User.objects.create_user(first_name=fn,last_name=ln,email=email,username=uname,password=pwd)
                res.save() 
                print("user created sucsessfully")



        else:
            print("password is incorrect")
            return redirect("loadregister")
        return redirect("/")
    else:
        return render(request,'register.html')






def loadlogin(request):
    if request.method == "POST" :
        un=request.POST["username"]
        pwd=request.POST["password"]
       
        print(un)
        print(pwd)
        user=auth.authenticate(username=un,password=pwd)
        print(user)
        if user is not None:
            print("hai")
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,'Data is invalied')
            return redirect('loadlogin')
    else:
        return render(request,'login.html')
        

def loadlogout(request):
    auth.logout(request)
    return redirect('/')
    