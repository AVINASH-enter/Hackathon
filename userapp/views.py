from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages, auth


def user(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirmpassword']

        # Check if passwords match
        if password != confirm_password:
            messages.error(request, "Passwords do not match.")
            return render(request, 'eventapp/reg.html')

        # Check if username or email already exists
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists.")
            return render(request, 'eventapp/reg.html')
        elif User.objects.filter(email=email).exists():
            messages.error(request, "Email is already registered.")
            return render(request, 'eventapp/reg.html')

        # If all validations pass, create a new user
        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()


        messages.success(request, "Registration successful!")
        return redirect('/')

    return render(request, 'eventapp/reg.html')


from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages  # Import messages framework


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            messages.success(request, "Login Successful")  # Success message
            return redirect('/')  # Redirect to events booking page (make sure this URL is correct)
        else:
            messages.error(request, "Invalid Credentials")  # Error message
            return render(request, 'eventapp/log.html')  # Stay on the same page

    return render(request, 'eventapp/log.html')


def logout(request):
    auth.logout(request)
    return redirect('/')
