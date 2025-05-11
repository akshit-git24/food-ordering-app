from django.db import models

from django.contrib.auth.models import User
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
# Create your models here.
class orders(models.Model):
    restaurant=models.ForeignKey(User, on_delete=models.CASCADE,default=True)
    item=models.CharField(max_length=50)
    body=models.TextField()
    price=models.IntegerField()

    def __str__(self):
        return self.item
    
class UserOrder(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_orders')
    order_item = models.ForeignKey(orders, on_delete=models.CASCADE, related_name='user_order_item')
    quantity = models.PositiveIntegerField(default=1)
    order_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=[
        ('PENDING', 'Pending'),
        ('COMPLETED', 'Completed'),
        ('CANCELLED', 'Cancelled')
    ], default='PENDING')
    
    def __str__(self):
        return f"{self.user.username} - {self.order_item.item} - {self.status}"
    
    def total_price(self):
        return self.quantity * self.order_item.price