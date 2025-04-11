from django.urls import path
from . import views
app_name='users'

urlpatterns = [
    path('register/',views.choice,name='choice'),
    path('customer/',views.customer,name='customer'),
    path('rest/',views.rest_reg,name='rest'),
    path('logout/',views.logout_view,name='logout'),
    path('',views.Homepage,name='Homepage'),
#   path('about/',views.About,name='About'),
]
