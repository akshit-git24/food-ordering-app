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
            
            # Redirect to customer dashboard
            next_url = request.GET.get('next', 'customer_dashboard')
            return redirect('Homepage')
    else:
        form = CustomerLoginForm()
    
    return render(request, 'login_user.html', {'form': form})

def restaurant_login_view(request):
    """View for restaurant login"""
    if request.method == 'POST':
        form = RestaurantLoginForm(data=request.POST)
        if form.is_valid():
            # The form.clean() method already authenticated the user
            # and stored it in form.user
            user = form.user
            login(request, user)
            
            # Redirect to restaurant dashboard
            next_url = request.GET.get('next', 'restaurant_dashboard')
            return redirect('Homepage')
    else:
        form = RestaurantLoginForm()
    return render(request, 'login_restaurant.html', {'form': form})

# Helper function to check user type
def get_user_type(user):
    if user.is_staff:
        return 'staff'
    else:
        return 'regular'

def choice_register(request):
     return render(request,"register_c.html")

def choice_login(request):
    return render(request,"login_c.html")

def logout_view(request):
    if request.method == "POST":
        logout(request)
        return redirect("users:Homepage")

def Dashboard(request):
    return render(request,'user_dash.html')

def Profile(request):
    return render(request,'user_profile.html')

def Homepage(request):
    return render(request, 'home.html')

#we use this to add form in our template
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