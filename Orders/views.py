from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from . import forms
from django.contrib.auth.models import User
from .models import orders,UserOrder
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

@login_required
def place_order(request,id):
    """
    View function to handle placing an order.
    
    This view is triggered when a user clicks the 'Place Order' button.
    It creates a new UserOrder instance linked to the current user and the selected order item.
    """
    # Get the order item by ID or return 404 if not found
    order_item = get_object_or_404(orders, id=id)
    
    # Handle POST request when form is submitted
    if request.method == 'POST':
        # Get quantity from form data, default to 1 if not provided
        quantity = int(request.POST.get('quantity', 1))
        user=request.user
        # Create a new user order
        
        existing_order = UserOrder.objects.filter(
                        user=request.user,
                        order_item=order_item,
                        status='PENDING'
                          ).exists()
        
        if existing_order:
            messages.warning(request, "You already have this item in your cart!")
        else:    
            user_order = UserOrder.objects.create(
                user=request.user,
                order_item=order_item,
                quantity=quantity,
                status='PENDING',
                order_date=user.date_joined
            )
        # Add success message
        messages.success(request, f"Your order for {quantity} {order_item.item}(s) has been placed successfully!")
        
        # Redirect to order confirmation or order history page
        # return redirect('User/user_profile.html', order_id=user_order.id)
    
    # If it's a GET request, show the order form
    context = {
        'order_item': order_item,
    }
    return render(request, 'home.html', context)