from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import AbstractUser
# Create your models here.
class RestUserManager(BaseUserManager):
    def create_user(self, username, email, password=None, **extra_fields):
        if not username:
            raise ValueError('The Username field must be set')
        
        email = self.normalize_email(email)
        user = self.model(username=username, email=email, **extra_fields)
        if password:
            user.set_password(password)  # This hashes the password
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