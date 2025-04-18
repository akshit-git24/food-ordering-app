from django import forms
from . import models
from django.forms import ModelForm, TextInput, EmailInput,NumberInput
class create_rest(forms.ModelForm):   
    password2 = forms.CharField(widget=forms.PasswordInput, label="Confirm Password")
    class Meta:
        model = models.rest_det
        fields =['username','email','password','rest_id','password2']
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
        def clean(self):
            cleaned_data = super().clean()
            password = cleaned_data.get('password')
            confirm_password = cleaned_data.get('confirm_password')
            
            if password and confirm_password and password != confirm_password:
                raise ValidationError("Passwords don't match")
            
            return cleaned_data
    
        def save(self, commit=True):
            # Remove confirm_password from the data as it's not a model field
            user = super().save(commit=False)
            user.set_password(self.cleaned_data['password'])  # Hash the password
            rest = super().save(commit=False)
            rest.user = user
            if commit:
                user.save()
            
            return user