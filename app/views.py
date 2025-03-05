from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from .models import User as CustomUser

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        details = request.POST['details']
        image = request.FILES.get('image')
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists")
            return redirect('register')
        user = User.objects.create_user(username=username, password=password)
        user.save()
        custom_user = CustomUser(user_name=username, password=password, details=details, image=image)
        custom_user.save()
        messages.success(request, "Registration successful! You can now log in.")
        return redirect('login')
    return render(request, 'app/register.html')

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.error(request, "Invalid credentials")
            return redirect('login')
    return render(request, 'app/login.html')

def index(request):
    if request.user.is_authenticated:
        user_details = CustomUser.objects.filter(user_name=request.user.username).first()
        return render(request, 'app/index.html', {'user_details': user_details})
    else:
        messages.info(request, "Please log in to view details")
        return redirect('login')

def user_logout(request):
    logout(request)
    return redirect('app/login')

def index(request):
    if request.user.is_authenticated:
        user_details = CustomUser.objects.filter(user_name=request.user.username).first()
        return render(request, 'app/index.html', {'user_details': user_details})
    else:
        messages.info(request, "Please log in to view details")
        return redirect('login')

def user_logout(request):
    logout(request)
    return redirect('login')
