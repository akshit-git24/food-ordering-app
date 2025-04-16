from django import forms 
from . import models

class orderform(forms.ModelForm):
    class Meta:
        model = models.orders
        fields=['item','body','price']
       