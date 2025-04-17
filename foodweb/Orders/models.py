from django.db import models
from User.models import rest_det
from django.contrib.auth.models import User
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
# Create your models here.
class orders(models.Model):
    restaurant=models.ForeignKey(rest_det, on_delete=models.CASCADE,default=True)
    item=models.CharField(max_length=50)
    body=models.TextField()
    price=models.IntegerField()

    def __str__(self):
        return self.item