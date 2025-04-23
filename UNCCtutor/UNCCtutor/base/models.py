from django.db import models
from django.contrib.auth.models import AbstractUser

# Custom user model
class User(AbstractUser):
    email = models.EmailField(unique=True, null=True)
    bio = models.TextField(null=True, default="I'm still setting up my profile!")
    avatar = models.ImageField(null=True, default="profile-pic-placeholder.png")
    classes = models.ManyToManyField('Classes', blank=True)
    skills = models.TextField(null=True,blank=True, default="I'm still setting up my profile!")
    currentYear = models.CharField(max_length=50, null=True, blank=True, default="I'm still setting up my profile!")
    tutor = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.username

# Tutor profile linked to user
class Tutor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='tutor_profile')
    expertise = models.TextField(null=True)
    rating = models.FloatField(null=True)

    def __str__(self):
        return f"Tutor Profile of {self.user.username}"

# Classes model
class Classes(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

