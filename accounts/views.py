from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login as djangoLogin, logout as djangoLogout
from django.contrib.auth.models import User
from home.models import Storie
from accounts.forms import Register

# Create your views here.


def login(request):

    next = request.GET.get('next')
    
    if request.user.is_authenticated:
        return redirect('/')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username = username, password = password)
        if user:
            djangoLogin(request, user)
            if next:
                return redirect(next)
            return redirect('/')
        else:
            messages.add_message(request, messages.WARNING, 'Username or password incorrect')
    return render(request, 'accounts/login.html')

def register(request):
    context = {
        'forms':Register()
    }
    if request.method == 'POST':
        data = Register(request.POST)
        if data.is_valid():
            user = data.save()
            user.set_password(user.password)
            user.save()
        else:
            print(data.errors)
            context['forms'] = data

    return render(request, 'accounts/register.html', context)

def logout(request):
    djangoLogout(request)
    return redirect('http://127.0.0.1:8000/accounts/login')

@login_required
def profile(request):
    context = {
        'my_stories':Storie.objects.filter(user = request.user)
    }
    return render(request, 'user-profile.html', context=context)