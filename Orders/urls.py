from django.urls import path
from . import views
app_name='orders'

urlpatterns = [
    path('',views.order_list,name="order_list"),
    # path('order/', views.place_order, name='place_order_with_item'),
    path('create/',views.create_order,name="new_order"),
    path('place_order/<int:id>/', views.place_order, name='place_order'),
]