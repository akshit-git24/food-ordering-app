from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import RegularUserProfile, StaffProfile

class RegularUserRegistrationForm(UserCreationForm):
    address = forms.CharField(widget=forms.Textarea, required=False)
    Contact_number = forms.CharField(max_length=10, required=False)
    date_of_birth = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}), required=False)
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
    
    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_staff = False  # Ensure user is not staff
        if commit:
            user.save()
            profile = RegularUserProfile(
                user=user,
                address=self.cleaned_data.get('address'),
                Contact_number=self.cleaned_data.get('Contact_number')
            )
            profile.save()
        return user

class StaffRegistrationForm(UserCreationForm):
    Restaurant_id = forms.CharField(max_length=20, widget=forms.TextInput(attrs={
            'class': 'form-control',
            'style': 'max-width: 3000px;',
           
        }))
    Restaurant_location= forms.CharField(max_length=100)
    Contact_number = forms.CharField(max_length=10, required=False)
    
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
    
    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_staff = True
        if commit:
            user.save()
            # Create the staff profile
            profile = StaffProfile(
                user=user,
                Restaurant_id=self.cleaned_data.get('Restaurant_id'),
                Restaurant_location=self.cleaned_data.get('Restaurant_location'),
                Contact_number=self.cleaned_data.get('Contact_number')
            )
            profile.save()
        return user
# from django import forms
# from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth import get_user_model
# from django.core.exceptions import ValidationError
# from .models import CustomerProfile, RestaurantProfile, UserProfile

# User = get_user_model()

# class CustomerSignUpForm(UserCreationForm):
#     email = forms.EmailField(required=True, help_text="Required. Enter a valid email address.")
#     phone_number = forms.CharField(max_length=15, required=False, 
#                                   help_text="Optional. Enter your phone number.")
#     address = forms.CharField(widget=forms.Textarea, required=False,
#                              help_text="Optional. Enter your address.")
#     city = forms.CharField(max_length=100, required=False)
#     state = forms.CharField(max_length=100, required=False)
#     zip_code = forms.CharField(max_length=10, required=False)
#     date_of_birth = forms.DateField(required=False, 
#                                    widget=forms.DateInput(attrs={'type': 'date'}),
#                                    help_text="Optional. Select your date of birth.")
#     dietary_preferences = forms.CharField(max_length=200, required=False,
#                                          help_text="Optional. List any dietary preferences.")
#     profile_picture = forms.ImageField(required=False)
    
#     class Meta:
#         model = User
#         fields = ('username', 'email', 'password1', 'password2')
    
#     def clean_password1(self):
#         password1 = self.cleaned_data.get('password1')
#         return password1
    
#     def save(self, commit=True):
#         user = super().save(commit=False)
#         user.email = self.cleaned_data.get('email')
#         if commit:
#             user.save()
#             # Set user type to customer
#             user.profile.user_type = 'customer'
#             if self.cleaned_data.get('profile_picture'):
#                 user.profile.profile_picture = self.cleaned_data.get('profile_picture')
#             user.profile.save()
            
#             # Save customer profile fields
#             user.customer.phone_number = self.cleaned_data.get('phone_number')
#             user.customer.address = self.cleaned_data.get('address')
#             user.customer.city = self.cleaned_data.get('city')
#             user.customer.state = self.cleaned_data.get('state')
#             user.customer.zip_code = self.cleaned_data.get('zip_code')
#             user.customer.date_of_birth = self.cleaned_data.get('date_of_birth')
#             user.customer.dietary_preferences = self.cleaned_data.get('dietary_preferences')
#             user.customer.save()
#         return user

# class RestaurantSignUpForm(UserCreationForm):
#     email = forms.EmailField(required=True, help_text="Required. Enter a valid email address.")
#     restaurant_name = forms.CharField(max_length=100, required=True,
#                                     help_text="Required. Enter your restaurant name.")
#     business_address = forms.CharField(widget=forms.Textarea, required=True,
#                                      help_text="Required. Enter your business address.")
#     contact_phone = forms.CharField(max_length=15, required=True,
#                                   help_text="Required. Enter your contact phone number.")
#     cuisine_type = forms.CharField(max_length=50, required=True,
#                                  help_text="Required. Enter your cuisine type.")
#     delivery_radius = forms.DecimalField(max_digits=5, decimal_places=2, required=False,
#                                        help_text="Optional. Enter your delivery radius in miles.")
#     business_hours = forms.JSONField(required=False, 
#                                    initial={"Mon": "9:00-21:00", "Tue": "9:00-21:00", "Wed": "9:00-21:00",
#                                           "Thu": "9:00-21:00", "Fri": "9:00-21:00", "Sat": "10:00-22:00", 
#                                           "Sun": "10:00-22:00"},
#                                    help_text="Optional. Enter your business hours.")
#     profile_picture = forms.ImageField(required=False)
    
#     class Meta:
#         model = User
#         fields = ('username', 'email', 'password1', 'password2')
    
#     def clean_password1(self):
#         password1 = self.cleaned_data.get('password1')
#         return password1
    
#     def save(self, commit=True):
#         user = super().save(commit=False)
#         user.email = self.cleaned_data.get('email')
#         if commit:
#             user.save()
#             # Set user type to restaurant
#             user.profile.user_type = 'restaurant'
#             if self.cleaned_data.get('profile_picture'):
#                 user.profile.profile_picture = self.cleaned_data.get('profile_picture')
#             user.profile.save()
            
#             # Save restaurant profile fields
#             user.restaurant.restaurant_name = self.cleaned_data.get('restaurant_name')
#             user.restaurant.business_address = self.cleaned_data.get('business_address')
#             user.restaurant.contact_phone = self.cleaned_data.get('contact_phone')
#             user.restaurant.cuisine_type = self.cleaned_data.get('cuisine_type')
#             user.restaurant.website = self.cleaned_data.get('website')
#             user.restaurant.delivery_radius = self.cleaned_data.get('delivery_radius')
#             user.restaurant.business_hours = self.cleaned_data.get('business_hours')
#             user.restaurant.save()
#         return user

# class UserProfileUpdateForm(forms.ModelForm):
#     profile_picture = forms.ImageField(required=False)
    
#     class Meta:
#         model = UserProfile
#         fields = ['profile_picture']

# class CustomerProfileUpdateForm(forms.ModelForm):
#     class Meta:
#         model = CustomerProfile
#         fields = ['phone_number', 'address', 'city', 'state', 'zip_code', 
#                  'date_of_birth', 'dietary_preferences']
#         widgets = {
#             'date_of_birth': forms.DateInput(attrs={'type': 'date'}),
#         }

# class RestaurantProfileUpdateForm(forms.ModelForm):
#     class Meta:
#         model = RestaurantProfile
#         fields = ['restaurant_name', 'business_address', 'contact_phone', 
#                  'cuisine_type', 'website', 'delivery_radius', 'business_hours']
# from django import forms
# from .models import RestaurantUser, CustomerUser
# from django.contrib.auth.forms import UserCreationForm

# class RestaurantRegistrationForm(UserCreationForm):
#     rest_id = forms.IntegerField(
#         widget=forms.NumberInput(attrs={
#             'class': 'form-control',
#             'style': 'max-width: 300px;',
#             'placeholder': 'Restaurant ID'
#         })
#     )
    
#     class Meta:
#         model = RestaurantUser
#         fields = ['username', 'email', 'rest_id', 'password1', 'password2']
#         widgets = {
#             'username': forms.TextInput(attrs={
#                 'class': 'form-control',
#                 'placeholder': 'Username'
#             }),
#             'email': forms.EmailInput(attrs={
#                 'class': 'form-control',
#                 'style': 'max-width: 300px;',
#                 'placeholder': 'Email'
#             }),
#         }

# class CustomerRegistrationForm(UserCreationForm):
#     phone_number = forms.CharField(
#         required=False,
#         widget=forms.TextInput(attrs={
#             'class': 'form-control',
#             'style': 'max-width: 300px;',
#             'placeholder': 'Phone Number (Optional)'
#         })
#     )
#     address = forms.CharField(
#         required=False,
#         widget=forms.Textarea(attrs={
#             'class': 'form-control',
#             'style': 'max-width: 300px;',
#             'placeholder': 'Address (Optional)',
#             'rows': 3
#         })
#     )
    
#     class Meta:
#         model = CustomerUser
#         fields = ['username', 'email', 'phone_number', 'address', 'password1', 'password2']
#         widgets = {
#             'username': forms.TextInput(attrs={
#                 'class': 'form-control',
#                 'placeholder': 'Username'
#             }),
#             'email': forms.EmailInput(attrs={
#                 'class': 'form-control',
#                 'style': 'max-width: 300px;',
#                 'placeholder': 'Email'
#             }),
#         }

# class LoginForm(forms.Form):
#     username = forms.CharField(widget=forms.TextInput(attrs={
#         'class': 'form-control',
#         'placeholder': 'Username'
#     }))
#     password = forms.CharField(widget=forms.PasswordInput(attrs={
#         'class': 'form-control',
#         'placeholder': 'Password'
#     }))                