from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from grain import settings
from django.core.mail import send_mail
def home(request):
    return render(request, "authentication/index.html")

def signup(request):
    if request.method == "POST":
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']
        if User.objects.filter(username=username):
            messages.error(request, "Username already exist! Please try some other username.")
            return redirect('home')
        
        if User.objects.filter(email=email).exists():
            messages.error(request, "Email Already Registered!!")
            return redirect('home')
        
        if len(username)>20:
            messages.error(request, "Username must be under 20 charcters!!")
            return redirect('home')
        
        if pass1 != pass2:
            messages.error(request, "Passwords didn't matched!!")
            return redirect('home')
        
        if not username.isalnum():
            messages.error(request, "Username must be Alpha-Numeric!!")
            return redirect('home')

        # Create a new user
        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.save()

        
        return redirect('signin')  # Replace 'home' with the actual URL name for the home page
        

    return render(request, "authentication/signup.html")

def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        pass1 = request.POST['pass1']
        
        user = authenticate(username=username, password=pass1)
        if user is not None:
            login(request, user)
            fname = user.first_name
            # messages.success(request, "Logged In Sucessfully!!")
            return render(request, "authentication/index.html",{"fname":fname})
        else:
           messages.error(request, "Bad Credentials!!")
           return redirect('home')
        
    return render(request, "authentication/signin.html")

def signout(request):
    # Add the signout logic here if neededQQ
    logout(request)
    messages.success(request, "Logged Out Successfully!!")
    return redirect('home')
def temp(request):
    return render(request, "authentication/temp.html")
def heap(request):
    return render(request, "authentication/heap.html")
def trade(request):
    return render(request, "authentication/trade.html")
def wheat(request):
    return render(request, "authentication/wheat.html")

def paddy(request):
    return render(request, "authentication/paddy.html")

def barley(request):
    return render(request, "authentication/barley.html")

def maize(request):
    return render(request, "authentication/maize.html")

def millet(request):
    return render(request, "authentication/millet.html")

def sorghum(request):
    return render(request, "authentication/sorghum.html")

