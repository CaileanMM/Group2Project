from django.shortcuts import render, redirect
from django.db.models import Q

from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import User, Classes, Review
from .forms import MyUserCreationForm, ReviewForm, UserProfileForm, SupportForm

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
    reviews = Review.objects.filter(tutor=user)

    avg_rating = user.rating

    context = {'user': user, 'bio': user.bio, 'userClasses': user.classes.all(),'skills':user.skills, 'currentYear':user.currentYear, 'avg_rating':avg_rating, 'reviews':reviews}
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

def extract_keywords(text):
    if not text:
        return[]
    
    words = text.lower().split()
    return [
        word.strip(".,?!")
        for word in words
        if len(word) >= 3
    ]

def get_tutors_by_skill(request):
    query = request.GET.get('q', '').strip()
    tutors = User.objects.all()
    
    if query:
        query_keywords = extract_keywords(query)
        if query_keywords:
            q_objects = Q()
            for keyword in query_keywords:
                q_objects |= Q(skills__icontains=keyword)
            tutors = tutors.filter(q_objects)

    return tutors

def tutorFinder(request):
    tutors = get_tutors_by_skill(request)
    context = {
        'tutors': tutors,
    }
    return render(request, 'base/tutor-finder.html', context)

    
@login_required(login_url='login')
def ChooseATutor(request):
    tutors = get_tutors_by_skill(request)
    context = {
        'tutors': tutors,
    }
    return render(request, 'base/choose-a-tutor.html', context)

def zoomPage(request):
    context = {}
    return render(request, 'base/zoom-page.html', context)

def support(request):
    if request.method == "POST":
        form = SupportForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            if request.user.is_authenticated:
                 message.user = request.user
            message.save()
            return redirect('home')
    else:
        form = SupportForm()        

    context = {'form' : form}
    return render(request, 'base/support.html', context)

def tutorProfile(request):
    context = {}
    return render(request, 'base/tutor-profile.html', context)

@login_required(login_url='login')
def rateTutor(request):
    user = request.user
    form = ReviewForm(request.POST)
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.save()
            tutor_reviewed = review.tutor
            messages.success(request, 'Your review has been submitted!')
            tutor_reviewed.rating = 0
            for review in Review.objects.filter(tutor=tutor_reviewed):
                tutor_reviewed.rating += review.rating
            tutor_reviewed.rating /= len(Review.objects.filter(tutor=tutor_reviewed))
            tutor_reviewed.rating = round(tutor_reviewed.rating, 2)
            tutor_reviewed.save()
            return redirect('home')
        else:
            messages.error(request, 'An error occurred while submitting your review.')
    else:
        form = ReviewForm()
    context = {'user': user, 'form': form}
    return render(request, 'base/rating-page.html', context)