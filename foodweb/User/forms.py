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
            'password':forms.TextInput(attrs={
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
        def clean(self):
            cleaned_data = super().clean()
            password = cleaned_data.get('password')
            confirm_password = cleaned_data.get('confirm_password')
            
            if password and confirm_password and password != confirm_password:
                 return self.add_error('confirm_password', "Passwords don't match")
                
            
            return cleaned_data
    
        def save(self, commit=True): 
            user = super().save(commit=False)
            password = self.cleaned_data.get('password')
            if password:
                user.set_password(password)
            
            if commit:
                user.save()
            
            return user