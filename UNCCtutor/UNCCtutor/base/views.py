from django.shortcuts import render
from django.db.models import Q
from django.contrib.auth.models import User


# Create your views here.

def loginPage(request):

    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POSt.get('password')

        try:
            user =User.objects.get(email=email)
        except:
            messages.error(request, 'incorrect uncc email')
    
    context = {}
    return render(request, 'base/login.html', context)