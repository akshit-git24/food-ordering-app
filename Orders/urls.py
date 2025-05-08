from django.urls import path
from . import views
app_name='orders'

urlpatterns = [
    path('',views.order_list,name="order_list"),
    path('create/',views.create_order,name="new_order")
]