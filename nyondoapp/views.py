from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required


# HOME PAGE
def home(request):
    return render(request, 'home.html')


# LOGIN VIEW
def login(request):

    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')
    return render(request, 'login.html')

       