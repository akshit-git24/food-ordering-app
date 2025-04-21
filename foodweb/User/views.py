from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login,logout
from . import forms
from . import models
from functools import wraps
from django.http import HttpResponseForbidden


# Create your views here.
def choice_register(request):
    return render(request,'register_c.html')

def choice_login(request):
    return render(request,'login_c.html')

def customer(request):
    if request.method == "POST":
        form=UserCreationForm(request.POST)#this
        if form.is_valid():                #and this validates the form and stops if there also anyone trying to register using same username as it exists already
            login(request,form.save())
            return redirect("users:Homepage")#here users:Home == {app_name defined in urls.py:name of the path}
    else:
        form=UserCreationForm()          
    return render(request,'cust.html',{"form":form})      #we use this to add form in our template



def login_customer(request):
    if request.method =="POST":
        form=AuthenticationForm(data=request.POST)
        if form.is_valid():
            login(request,form.get_user())#we login 
            if "next" in request.POST:
                return redirect(request.POST.get('next'))
            else:
                return redirect("orders:order_list")
    else:
        form=AuthenticationForm()    
    return render(request,'login_user.html',{"form":form})

def rest_reg(request):
    if request.method=="POST":
        form=forms.create_rest(request.POST,request.FILES)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            confirm_password = form.cleaned_data.get('confirm_password')
            rest_id = form.cleaned_data.get('rest_id')
            
            user = models.rest_det.objects.create_user(
                username=username,
                email=email,
                password=password,
                rest_id=rest_id,
                confirm_password=confirm_password
            ) 
            if user:
                auth_user = authenticate(request, username=username, password=password)
                if auth_user:
                    login(request, auth_user)
                    return redirect('orders:order_list')
                else:
                    form.add_error(None, "You aren't autherised")
            else:
                form.add_error(None, "User creation failed") 
            
    else:
          form=forms.create_rest()
    context = {
        'user': request.user,
        'form':form
                }       
    return render(request,'rest.html',context)    

 
def logout_view(request):
    if request.method =="POST":
        logout(request)
        return redirect("users:Homepage")

def Homepage(request):
    return render(request,'home.html')


#we use this to add form in our template
# user=authenticate(request, username=username, password=password)     
#             login(request, user)
#             return redirect('orders:order_list')