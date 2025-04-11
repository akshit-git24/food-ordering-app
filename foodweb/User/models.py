from django.db import models

# Create your models here.
class rest_det(models.Model):
    username=models.CharField(max_length=75)
    email=models.EmailField(blank=False)
    rest_id=models.CharField(max_length=75,primary_key=True)
    password=models.CharField(max_length=75)
    
    def __init__(self):
        return self.username
       