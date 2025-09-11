from django.db import models
from django.utils import timezone
from django.contrib.auth.models import (
    BaseUserManager,AbstractBaseUser,PermissionsMixin
)

# Creating custom user manager for custom user 
class CustomUserManager(BaseUserManager):
    def createuser(self,email,full_name,role='User',password=None,**extra_fields):
        email=self.normalize_email(email=email)
        user=self.model(email=email,full_name=full_name,role=role,**extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def createsuperuser(self,email,full_name,password=None,**extra_fields):
        extra_fields.setdefault('role','Admin')
        extra_fields.setdefault('is_staff',True)
        extra_fields.setdefault('is_superuser',True)

        if extra_fields.get("role") != "Admin":
            print("Superuser role must be Admin")
            return
        
        return self.createuser(email=email,full_name=full_name,password=password,**extra_fields)


# Create your models here.
class CustomUser(AbstractBaseUser,PermissionsMixin):
    USER_ROLE = [
        ('Admin','Admin'),
        ('User','User')
    ]

    email=models.EmailField(unique=True)
    full_name=models.CharField(max_length=50)
    date_joined=models.DateField(default=timezone.now)
    role=models.TextField(max_length=40,choices=USER_ROLE,default='User')
    is_active=models.BooleanField(default=True)
    is_staff=models.BooleanField(default=False)

    obj = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['full_name']

    def __str__(self):
        return f'{self.full_name}:{self.role}'
    