from django.urls import path
from . import views
app_name='users'

urlpatterns = [
    path('register_choice/',views.choice_register,name='choice_register'),
    path('login_choice/',views.choice_login,name='choice_login'),
    path('customer/',views.customer,name='customer_reg'),
    path('rest/',views.rest_reg,name='rest_reg'),
    path('login_customer/',views.login_customer,name='rest_reg'),
    path('logout/',views.logout_view,name='logout'),
    path('',views.Homepage,name='Homepage'),
]
