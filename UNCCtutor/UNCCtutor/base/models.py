from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class User(AbstractUser):
    # name = models.CharField(max_length=200, null=True)
    email = models.EmailField(unique=True,  null=True)
    bio = models.TextField(null=True)

    avatar= models.ImageField(null=True, default="profile-pic-placeholder.png")

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']