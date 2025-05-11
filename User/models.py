from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.validators import RegexValidator, MinLengthValidator,MaxLengthValidator
from django.core.exceptions import ValidationError
import re

class RegularUserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='regular_profile')
    address = models.TextField(blank=True, null=True)
    Contact_number = models.CharField(max_length=15, blank=True, null=True,unique=True)
    date_of_birth = models.DateField(blank=True, null=True)
    
    def __str__(self):
        return f"Regular User: {self.user.username}"

# Profile model for staff users or we can say for Restaurants
class StaffProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='staff_profile')
    Restaurant_id = models.IntegerField(unique=True,default=True)
    Restaurant_name=models.CharField(max_length=25,default=False,null=False)
    Restaurant_location = models.CharField(max_length=100)
    Contact_number = models.CharField(max_length=10, blank=True, null=True)
    
    def __str__(self):
        return f" {self.user.username}--{self.Restaurant_name}--{self.Restaurant_id}"
# to add password strongness
    # def validate_password_strength(password):
    #      """
    #     Validates that a password meets minimum requirements:
    #     - At least 8 characters long
    #     - Contains at least one digit
    #     - Contains at least one uppercase letter
    #     - Contains at least one lowercase letter
    #     - Contains at least one special character
    #     """
    #     if len(password) < 8:
    #         raise ValidationError("Password must be at least 8 characters long.")
        
    #     if not re.search(r'\d', password):
    #         raise ValidationError("Password must contain at least one digit.")
        
    #     if not re.search(r'[A-Z]', password):
    #         raise ValidationError("Password must contain at least one uppercase letter.")
        
    #     if not re.search(r'[a-z]', password):
    #         raise ValidationError("Password must contain at least one lowercase letter.")
        
    #     if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
    #         raise ValidationError("Password must contain at least one special character.")