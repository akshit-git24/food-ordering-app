from django import forms
from . import models
from django.contrib.auth.hashers import make_password
class create_rest(forms.ModelForm):   
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'style': 'max-width: 300px;',
        'placeholder': 'Confirm Password'
    }), label="Confirm Password")
    class Meta:
        model = models.rest_det
        fields =['username','email','password','rest_id','confirm_password']
        widgets ={
            'username': forms.TextInput(attrs={
                'class': "form-control",
                'placeholder': 'UserName'
                }),
            'email':forms.EmailInput(attrs={
                'class': "form-control", 
                'style': 'max-width: 300px;',
                'placeholder': 'Email'
                }),
            'password':forms.PasswordInput(attrs={
                'class': "form-control", 
                'style': 'max-width: 300px;',
                'type':'password',
                'placeholder': 'password'
                }),
            'rest_id':forms.NumberInput(attrs={
                'class': "form-control", 
                'style': 'max-width: 300px;',
                'placeholder': 'Restaurant ID'
                }),
        }

# class LoginForm(forms.Form):
#     username = forms.CharField(widget=forms.TextInput(attrs={
#         'class': 'form-control',
#         'placeholder': 'Username'
#     }))
#     password = forms.CharField(widget=forms.PasswordInput(attrs={
#         'class': 'form-control',
#         'placeholder': 'Password'
#     }))                