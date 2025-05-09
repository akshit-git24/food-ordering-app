from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from . import forms
from django.contrib.auth.models import User
from .models import orders
from functools import wraps
from User import models
from django.http import HttpResponseForbidden
# from .decorators import rest_det_required
# Create your views here.
def is_rest(user):
    return user.is_staff

def order_list(request):
    order=orders.objects.all().order_by('-price')
    return render(request,'order_list.html',{'order':order})

@user_passes_test(is_rest)
def create_order(request):
      if request.method=="POST":
         form=forms.orderform(request.POST,request.FILES)
         if form.is_valid():
             new_order=form.save(commit=False)
             new_order.restaurant=request.user
             new_order.save()
             return redirect('orders:order_list')
      else:
          form=forms.orderform()
      return render(request,'create_order.html',{'form':form})    
