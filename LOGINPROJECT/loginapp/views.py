from django.shortcuts import redirect, render
from .import forms
from .import models
from django.http import HttpResponse,request
import random


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
            p1=request.POST['password1']
            p2=request.POST['password2']
            l=len(request.POST['phoneno'])
            print(p1,p2)
            if p1!=p2:
               return render(request,"register.html",{"data":obj,"info":"password didn't match"})  
            elif l!=10:
               return render(request,"register.html",{"data":obj,"leninfo":'phone no should contain 10 digits'}) 
            obj.save()
            return redirect ("/home/login")

            #if p1==p2 :
             #  obj.save()
              # return redirect ("/home/login")
            #else:
             #   return render(request,"register.html",{"data":obj,"info":'password didn''t match',"leninfo":'phone no should contain 10 digits'}) 

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
              except ValueError as ve:    
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
        ph=request.POST['phno']  
        p1=request.POST['pass1']
        p2=request.POST['pass2']
        if p1==p2:
            obj=models.logintable.objects.get(phoneno_exact=ph)

            obj.password1=p1
            obj.password2=p1
             #obj=?
             #obj.password1=p1
             #obj.password2=p1
            print(obj)
            return render(request,"verify.html")

    return render(request,"forgotpassword.html")

def verifying(request):
    if request.method=='POST':
        num=random.randint(100000,999999)
        print (num)
        #val=request.POST['otptext']
        #if val==num:
        #    print (val)
        #    print (num)
        #    return redirect("/home/login")
        #else:
        return render(request,"verify.html",{"data":num})
        #else:    
        #  return render(request,"verify.html")
    return render(request,"verify.html")