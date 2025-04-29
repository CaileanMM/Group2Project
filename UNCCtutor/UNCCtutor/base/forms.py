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

class SelectTutorForm(forms.Form):
    user = forms.ModelChoiceField(queryset=User.objects.none())

    def __init__(self, *args, **kwargs):
        tutor = kwargs.pop('tutor', False)
        super().__init__(*args, **kwargs)
        if tutor:
            self.fields['user'].queryset = User.objects.filter(tutor=True)
        else:
            self.fields['user'].queryset = User.objects.filter(tutor=False)
