from django.shortcuts import render, redirect
from django.db.models import Q
from django.contrib import messages


from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User 

from .models import User
from .forms import MyUserCreationForm


# Create your views here.
def home(request):
    return render(request, 'base/landing.html')

def loginPage(request):

    page = 'login'
    #if(request.user.is_authenticated)
    #    return redirect('')

    if request.method == 'POST':
        email = request.POST.get('email').lower()
        password = request.POST.get('password')

        try:
            user = User.objects.get(email=email)
        except:
            messages.error(request, 'incorrect uncc email')
        
        user = authenticate(request, email=email, password=password)

        if user is not None:
            login(request, user)
            #  return redirect()
        else:
            messages.error(request, 'Email OR password does not exist')
    
    context = {}
    return render(request, 'base/login.html', context)


def registerPage(request):

    form = MyUserCreationForm()

    if request.method == 'POST':
        form = MyUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, "An error occured dufring registeration")


    return render(request, 'base/register.html', {'form':form})


def userProfile(request):
    context = {}
    return render(request, 'base/profile.html', context)

def editProfile(request):
    context = {}
    return render(request, 'base/edit-profile.html', context)

def editClasses(request):
    context = {}
    return render(request, 'base/edit-classes.html', context)


def tutorFinder(request):
    context = {}
    return render(request, 'base/tutor-finder.html', context)