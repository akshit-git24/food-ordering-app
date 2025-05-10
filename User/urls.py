from django.urls import path
from . import views

app_name = 'users'

urlpatterns = [
    path('register_choice/', views.choice_register, name='choice_register'),
    path('login_choice/', views.choice_login, name='choice_login'),
    path('customer/', views.customer_signup, name='customer_registration'),
    path('rest/', views.restaurant_signup, name='restaurant_registration'),
    path('customer/login/', views.customer_login_view, name='customer_login'),
    path('restaurant/login/', views.restaurant_login_view, name='restaurant_login'),
    path('logout/', views.logout_view, name='logout'),
    path('', views.Homepage, name='Homepage'),
    path('cust/dash/', views.Dashboard, name='Dashboard'),
    path('cust/profile/', views.Profile, name='profile'),
]
