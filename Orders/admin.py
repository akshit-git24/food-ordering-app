from django.contrib import admin
from .models import orders,UserOrder
# Register your models here.
admin.site.register(orders)
admin.site.register(UserOrder)