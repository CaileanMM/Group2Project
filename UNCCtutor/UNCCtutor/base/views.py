from django.shortcuts import render, redirect
from django.db.models import Q
from django.contrib import messages

from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import User
from .forms import MyUserCreationForm, UserProfileForm


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
            return redirect('home')
        else:
            messages.error(request, 'Email OR password does not exist')
    
    context = {}
    return render(request, 'base/login.html', context)


def registerPage(request):

    form = MyUserCreationForm(request.POST) 
    if request.method == 'POST':
        
        print(form.errors)
        if form.is_valid():
            user = form.save(commit=True)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, "An error occurred during registration")
    else:
        form = MyUserCreationForm()
    return render(request, 'base/register.html', {'form':form})

@login_required(login_url='login')
def userProfile(request, pk):

    user = User.objects.get(id=pk)
    bio = User.bio
    context = {'user': user, 'bio': bio}
    return render(request, 'base/profile.html', context)

def logoutUser(request):
    logout(request)
    return redirect('home')

@login_required(login_url='login')
def editProfile(request, pk):
    user = request.user
    form = UserProfileForm(request.POST, instance=user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('user-profile', pk=user.id)

    return render(request, 'base/edit-profile.html', {'form': form})

def editClasses(request):
    context = {}
    return render(request, 'base/edit-classes.html', context)


def tutorFinder(request):
    context = {}
    return render(request, 'base/tutor-finder.html', context)
    
def ChooseATutor(request):
    context = {
        "Test" : ["Bob","William","Stephen"],
    }
    return render(request, 'base/choose-a-tutor.html', context)

def zoomPage(request):
    context = {}
    return render(request, 'base/zoom-page.html', context)

def support(request):
    context = {}
    return render(request, 'base/support.html', context)

def tutorProfile(request):
    context = {}
    return render(request, 'base/tutor-profile.html', context)