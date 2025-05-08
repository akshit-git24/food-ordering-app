from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError

# Create your models here.
class RestUserManager(BaseUserManager):
    def create_user(self, username, email, password=None,confirm_password=None, **extra_fields):
        if not username:
            raise ValueError('The Username field must be set')
        
        email = self.normalize_email(email)
        user = self.model(username=username, email=email, **extra_fields)
        if confirm_password is not None and password != confirm_password:
            raise ValidationError("Passwords don't match")
        
        # Here I'm Removing confirm_password from extra_fields if  exists in it.
        if 'confirm_password' in extra_fields:
            extra_fields.pop('confirm_password')
            
        user = self.model(username=username, email=email, **extra_fields)
        
        if password:
            user.set_password(password)  # password hashing is done here by logic written manually
        
        user.save(using=self._db)
        return user
    
    def create_superuser(self, username, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        
        return self.create_user(username, email, password, **extra_fields)

class rest_det(AbstractBaseUser):

    REQUIRED_FIELDS = ['email']
    is_active = models.BooleanField(default=True)
    USERNAME_FIELD = 'username'
    username=models.CharField(max_length=75,unique=True)
    email=models.EmailField(unique=True)
    rest_id=models.IntegerField(primary_key=True)
    objects = RestUserManager()
    def __str__(self):
        return str(self.username)
    

    # groups = models.ManyToManyField(
    #     'auth.Group',
    #     related_name='rest_det_set',  # Changed from default 'user_set'
    #     blank=True,
    #     help_text='The groups this user belongs to.',
    #     verbose_name='groups',
    # )
    # user_permissions = models.ManyToManyField(
    #     'auth.Permission',
    #     related_name='rest_det_set',  # Changed from default 'user_set'
    #     blank=True,
    #     help_text='Specific permissions for this user.',
    #     verbose_name='user permissions',
    # )       


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