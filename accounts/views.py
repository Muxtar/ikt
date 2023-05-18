from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login as djangoLogin, logout as djangoLogout
from django.contrib.auth.models import User
from home.models import Storie
from accounts.models import Profile
from accounts.forms import Register
from django.contrib.auth.views import (PasswordResetView, 
                                       PasswordResetConfirmView,
                                       PasswordResetDoneView
                                       )

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
            return redirect(reverse_lazy('login'))
        else:
            context['forms'] = data

    return render(request, 'accounts/register.html', context)

def logout(request):
    djangoLogout(request)
    return redirect('http://127.0.0.1:8000/accounts/login')

@login_required
def profile(request):
    if request.method == 'POST':
        image = request.FILES.get('image')
        with open(f'/home/mb/Desktop/iktlab/media/profile/{image.name}', 'wb') as f:
            f.write(image.read())
            userProfile = Profile.objects.get(user_id = request.user.id) 
            userProfile.img = 'profile/'+image.name
            userProfile.save()
    context = {
        'my_stories':Storie.objects.filter(user = request.user)
    }
    return render(request, 'user-profile.html', context=context)

class MyPasswordResetView(PasswordResetView):
    template_name = 'accounts/forget_password.html'
