from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
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

class TutorCard(models.Model):
    host = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=200)
    rating = models.IntegerField(default=0)

    def __str__(self):
        return self.name


# Classes model
class Classes(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class Review(models.Model):
    tutor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='Tutors', limit_choices_to={'tutor': True})
    rating = models.IntegerField(default=1, validators=[
        MinValueValidator(1),
        MaxValueValidator(5)
    ])
    comment = models.TextField(max_length=200, null=True, blank=True, default="Add a comment!")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.tutor} Review"

