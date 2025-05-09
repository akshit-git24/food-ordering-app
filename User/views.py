from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .forms import (
    StaffRegistrationForm,RegularUserRegistrationForm
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
            messages.success(request, f"Staff account created for {user.username}!")
            return redirect('Homepage')
    else:
        form = StaffRegistrationForm()
    return render(request, 'rest.html', {'form': form})

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