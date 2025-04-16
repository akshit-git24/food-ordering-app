from django import forms
from . import models
from django.forms import ModelForm, TextInput, EmailInput,NumberInput
class create_rest(forms.ModelForm):   
    password2=forms.CharField()
    class Meta:
        model = models.rest_det
        fields =['username','email','password','rest_id','password2']
        widgets =    widgets = {
            'username': forms.TextInput(attrs={
                'class': "form-control",
                'placeholder': 'UserName'
                }),
            'email':forms.EmailInput(attrs={
                'class': "form-control", 
                'style': 'max-width: 300px;',
                'placeholder': 'Email'
                }),
            'password':forms.TextInput(attrs={
                'class': "form-control", 
                'style': 'max-width: 300px;',
                'type':'password',
                'placeholder': 'password'
                }),
            'password2':forms.TextInput(attrs={
                'class': "form-control", 
                'style': 'max-width: 300px;',
                'type':'password',
                'placeholder': 'Confirm Password',
                }),
            'rest_id':forms.NumberInput(attrs={
                'class': "form-control", 
                'style': 'max-width: 300px;',
                'placeholder': 'Restaurant ID'
                }),
        }