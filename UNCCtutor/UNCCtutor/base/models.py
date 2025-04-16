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


class Tutor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='tutor_profile')
    expertise = models.TextField(null=True)
    rating = models.FloatField(null=True)

    def __str__(self):
        return f"Tutor Profile of {self.user.username}"

class Classes(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name