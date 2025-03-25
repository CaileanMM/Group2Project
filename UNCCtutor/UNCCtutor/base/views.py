from django.shortcuts import render
from django.db.models import Q


# Create your views here.

def loginPage(request):
    context = {}
    return render(request, 'base/login.html', context)