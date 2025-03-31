from django.shortcuts import render
from django.db.models import Q
from django.contrib.auth.models import User


# Create your views here.
def home(request):
    return render('Home page')

def loginPage(request):

    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            user = User.objects.get(email=email)
        except:
            messages.error(request, 'incorrect uncc email')
    
    context = {}
    return render(request, 'base/login.html', context)




def RegisterPage(request):

    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            user = User.objects.get(email=email)
        except:
            messages.error(request, 'incorrect uncc email')
    
    context = {}
    return render(request, 'base/register.html', context)

def userProfile(request):
    context = {}
    return render(request, 'base/templates/base/user-profile.html', context)

def tutorFinder(request):
    context = {}
    return render(request, 'base/tutor-finder.html', context)