from django.db import models

from django.contrib.auth.models import (
    AbstractBaseUser,
    PermissionsMixin
)

from .managers import CustomUserManager

class User(AbstractBaseUser,PermissionsMixin):
    email=models.EmailField(
        unique=True
    )
    username=models.CharField(
        max_length=100,unique=True
    )
    first_name=models.CharField(max_length=100,blank=True)
    last_name=models.CharField(max_length=100,blank=True)
    avatar=models.ImageField(upload_to="avatars/",blank=True,null=True)
    bio=models.TextField(blank=True)
    job_title=models.CharField( max_length=150,blank=True)
    is_active=models.BooleanField(default=True)
    is_staff=models.BooleanField(default=False)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    objects= CustomUserManager()
    USERNAME_FIELD="email"
    REQUIRED_FIELDS=["username"]

    def __str__(self):
        return self.email