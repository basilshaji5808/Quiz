from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('quiz:home')
        else:
            messages.info(request, 'User is invalid')
            return redirect('user:login')
    return render(request, 'login.html')


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        cpassword = request.POST['password1']
        if password == cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username is already exist')
                return redirect('user:register')
            if User.objects.filter(email=email).exists():
                messages.info(request, 'Email-ID is already exists')
                return redirect('user:register')
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()
                return redirect('user:login')
        else:
            messages.info(request, 'Password is not matched')
            return redirect('user:register')
        return redirect('/')
    return render(request, 'register.html')


def logout(request):
    auth.logout(request)
    return redirect('quiz:home')
