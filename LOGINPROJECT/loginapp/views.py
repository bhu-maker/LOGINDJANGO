
from re import L
from django.shortcuts import redirect, render
from .import forms
from .import models
from django.http import HttpResponse,request


# Create your views here.
def registering(request):
    obj=forms.loginform()
    if request.method=='POST':
        obj=forms.loginform(request.POST)
        print(request.POST)
        if obj.is_valid():
            #mobj1=models.logintable.objects.get(instance=request.POST)
            #print(mobj1.password1)
            #error handling 
            obj.save()
            return redirect ("/home/login")
    return render(request,"register.html",{"data":obj})  


def logging(request):
    if request.method=='POST':
      e=request.POST['emph']       
      pas=request.POST['pass']
      print(e,pas)
      print(type(e))
      try:
          obj=models.logintable.objects.get(email__exact=e)
      except  models.logintable.DoesNotExist:  
              try :
                 obj=models.logintable.objects.get(phoneno__exact=e)
              except  models.logintable.DoesNotExist:  
                return render(request,"login.html")  
           
      if pas==obj.password1:
         print(obj)
         print(obj.username)
         print(request.POST)
         return  redirect("/home/")
      return render(request,"login.html")   
    return render(request,"login.html")


def forgotting(request):
    if request.method=='POST':
        p1=request.POST['pass1']
        p2=request.POST['pass2']
        if p1==p2:
             return  redirect("/home/")
             #obj=?
             #obj.password1=p1
             #obj.password2=p1
    return render(request,"forgotpassword.html")
