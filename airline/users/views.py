from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
# Create your views here.

def index(request):
    if not request.user.is_authenticated:
        return redirect('uers:login')
    return render(request, 'users/users.html')


def login_view(request):
    if request.method == 'POST':
        # Process login form submission
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('flights:index') # Success! Go to flights.
        else: 
            # Failure! Re-render the SAME page with an error message.
            return render(request, 'users/login.html', 
                          {'message': 'Invalid credentials'})
    else:

        return render(request, 'users/login.html')

def logout_view(request):
    logout(request)
    return redirect('users:login')

def register_view(request):
    if request.method == 'POST':
        # Process registration form submission
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirmation = request.POST['confirmation']
        
        #basic validation
        if password != confirmation:
            return render (request, "users/register.html",{"message":"Passwords dont match"})
        
        #check if username already exits 
        if User.objects.filter(username=username).exists():
            return render (request, "users/register.html",{"message": " Username exists "})
        
        #create a user 
        user = User.objects.create_user(username, email, password)
        user.save()

        #log them in and go to flights page 
        login(request, user)
        return redirect ("flights:index")
    
    return render(request, "users/register.html")
