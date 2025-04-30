from typing import Self
from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from .models import User
from .models import Review

class MyUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'tutor']

class UserProfileForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'bio', 'skills', 'currentYear']
        widgets = {
            'bio': forms.Textarea(attrs={'rows': 3}),
            'skills': forms.Textarea(attrs={'rows': 2}),
            'currentYear': forms.TextInput(attrs={'placeholder': 'e.g. Sophomore'}),
        }

class ReviewForm(forms.Form):
    
    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request')
        super(ReviewForm, self).__init__(*args, **kwargs)
        self.fields['student'].initial = User.objects.get(user=self.request.user)
    
    class Meta:
        model = Review
        fields = ['tutor', 'student', 'rating', 'comment']
        widgits = {
        'tutor': forms.ModelChoiceField(queryset=User.objects.filter(tutor=True), empty_label="Select a tutor"),
        'rating': forms.IntegerField(min_value=1, max_value=5),
        'comment': forms.Textarea(attrs={'rows': 3} | {'placeholder': 'Write your review here...'}, max_length=200, required=False),
        'student': forms.HiddenInput(),
        }