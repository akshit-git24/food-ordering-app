from django.shortcuts import render,redirect
from .models import rest_det
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import login,logout
from . import forms
# Create your views here.
def choice(request):
    return render(request,'register_c.html')

def customer(request):
    return render(request,'cust.html')

def rest_reg(request):
    if request.method=="POST":
        form=forms.create_rest(request.POST,request.FILES)
        if form.is_valid():
           
              reg=form.save(commit=False)
            #   reg.username=request.user
              reg.save()
            # login(request,form.get_user())
              return redirect("orders:order_list")
    else:
          form=forms.create_rest()
    return render(request,'rest.html',{'form':form})    
# def log_reg(request):   
# def rest_reg(request):
#     if request.method=='POST':
#         username=request.POST['username']
#         email=request.POST['email']
#         restaurant_id=request.POST.get('rest_id')
#         password=request.POST.get('password')
#         password2 = request.POST.get('confirm_password')

#         if rest_det.objects.filter(email=email).exists():
#             messages.info(request,'Email already exist')
#         elif rest_det.objects.filter(rest_id=restaurant_id).exists():
#              messages.info(request,'restaurant already exist')
#         else:
#             if password==password2:
#                 restraunt=rest_det.objects.create(
#                     username=username,email=email,
#                     rest_id=restaurant_id,
#                     password=password
#                     )
#                 restraunt.save()
#                 login(request)
#                 return render(request,'home.html')
#             else:
#                 messages.info(request,"password not the same")
           
#     else:   
#         return render(request,'rest.html')

def logout_view(request):
    if request.method =="POST":
        logout(request)
        return redirect("users:Homepage")

def Homepage(request):
    return render(request,'home.html')
