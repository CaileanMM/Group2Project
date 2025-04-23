from django.shortcuts import render, redirect
from django.db.models import Q
from django.contrib import messages

from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import User, Classes
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

    context = {'user': user, 'bio': user.bio, 'userClasses': user.classes.all(),'skills':user.skills, 'currentYear':user.currentYear}
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

    else:
        form = UserProfileForm(instance=user)

    context = {'form': form, 'user': user}

    return render(request, 'base/edit-profile.html', context)

@login_required(login_url='login')
def editClasses(request):
    user = request.user
    all_classes = Classes.objects.all()

    if request.method == 'POST':
        # Get the selected class IDs from the form (checkboxes)
        selected_class_ids = request.POST.getlist('classes')
        
        # Update the user's classes (add/remove classes)
        user.classes.set(selected_class_ids)
        
        # Show a success message
        messages.success(request, 'Your classes have been updated successfully!')
        
        # Redirect to the user profile page after the update
        return redirect('user-profile', pk=user.id)  # Redirect to the profile page

    # Pass both the current classes and all available classes to the template
    return render(request, 'base/edit-classes.html', {
        'user_classes': user.classes.all(),  # Get current classes the user is enrolled in
        'all_classes': all_classes,  # Get all available classes
    })


def tutorFinder(request):
    context = {}
    return render(request, 'base/tutor-finder.html', context)
    
@login_required(login_url='login')
def ChooseATutor(request):
    tutorName1 = "John"
    tutorName2 = "William"
    tutorName3 = "Stephen"
    tutorName4 = "Hanie"
    context = {
        "Name" : [tutorName1,tutorName2,tutorName3,tutorName4],
        "Major" : ["Math","Science","English", "Computer"],
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