from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login as djangoLogin, logout as djangoLogout
from django.contrib.auth.models import User
# Create your views here.


def login(request):
    if request.user.is_authenticated:
        return redirect('/')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username = username, password = password)
        if user:
            djangoLogin(request, user)
            return redirect('/')
        else:
            messages.add_message(request, messages.WARNING, 'Username or password incorrect')
    return render(request, 'accounts/login.html')

def register(request):
    pass

def logout(request):
    djangoLogout(request)
    return redirect('http://127.0.0.1:8000/accounts/login')