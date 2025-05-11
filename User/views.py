from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .forms import (
    StaffRegistrationForm,RegularUserRegistrationForm,RestaurantLoginForm,CustomerLoginForm
)
from .models import StaffProfile,RegularUserProfile
from Orders.models import orders,UserOrder
def customer_signup(request):
    if request.method == 'POST':
        form = RegularUserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, f"Regular user account created for {user.username}!")
            return redirect('Homepage')
    else:
        form = RegularUserRegistrationForm()
    return render(request, 'cust.html', {'form': form})

def restaurant_signup(request):
    if request.method == 'POST':
        form = StaffRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, f"Restaurant account created for {user.username}!")
            return redirect('Homepage')
    else:
        form = StaffRegistrationForm()
    return render(request, 'rest.html', {'form': form})

def customer_login_view(request):
    """View for customer login"""
    if request.method == 'POST':
        form = CustomerLoginForm(data=request.POST)
        if form.is_valid():
            user = form.user
            login(request, user)

            next_url = request.GET.get('next', 'customer_dashboard')
            return redirect('Homepage')
    else:
        form = CustomerLoginForm()
    
    return render(request, 'login_user.html', {'form': form})

def restaurant_login_view(request):
    if request.method == 'POST':
        form = RestaurantLoginForm(data=request.POST)
        if form.is_valid():
            user = form.user # The form.clean() method already authenticated the user                           
            login(request, user)  # and stored it in form.user
            
            next_url = request.GET.get('next', 'Dashboard')
            return redirect('Homepage')
    else:
        form = RestaurantLoginForm()
    return render(request, 'login_restaurant.html', {'form': form})

def choice_register(request):
     return render(request,"register_c.html")

def choice_login(request):
    return render(request,"login_c.html")

def logout_view(request):
    if request.method == "POST":
        logout(request)
        return redirect("users:Homepage")
    
@login_required
def Dashboard(request):
    user=request.user
    staff_profile = StaffProfile.objects.get(user=request.user)
    
    ''' to get data from user model firstly,
        user=request.user
        and pass the context and then use it as normally'''
    
    # Query parameters from URL
    # query_param = request.GET.get('param', None)
    # if query_param:
    #     filtered_data = filtered_data.filter(field_name__contains=query_param)
    
    context = {
        'data': staff_profile,
        'user': user,
    }
    
    return render(request,'user_dash.html', context)

@login_required
def Profile(request):
    user=request.user
    user_profile = RegularUserProfile.objects.get(user=request.user)
    user_order_det=UserOrder.objects.filter(user=request.user)
    context = {
        'data': user_profile,
        'user': user,
        'user_order_det':user_order_det,
    }
    return render(request,'user_profile.html',context)

def Homepage(request):
    return render(request, 'home.html')

#I use this to add form in our template
# user=authenticate(request, username=username, password=password)     
#             login(request, user)
#             return redirect('orders:order_list')
# class CustomerSignUpView(CreateView):
#     form_class = CustomerSignUpForm
#     template_name = 'User/login_user.html'
#     success_url = reverse_lazy('Homepage')
    
#     def form_valid(self, form):
#         user = form.save()
#         login(self.request, user)
#         return redirect(self.success_url)

# class RestaurantSignUpView(CreateView):
#     form_class = RestaurantSignUpForm
#     template_name = 'User/rest.html'
#     success_url = reverse_lazy('Homepage')
    
#     def form_valid(self, form):
#         user = form.save()
#         login(self.request, user)
#         return redirect(self.success_url)
# 
# # The form.clean() method already authenticated the user
            # and stored it in form.user