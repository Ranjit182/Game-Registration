from django.shortcuts import render,HttpResponse,redirect
from app1.models import users
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

# Create your views here.
def homepage(request):
    responce=render(request,'home.html')
    return responce
def dash(request):
    return render(request,'dash.html')

def signuppage(request):
    if request.method == 'POST': 
        uname = request.POST.get('username')
        email = request.POST.get('email')
        pass1 = request.POST.get('pass1')
        pass2 = request.POST.get('pass2')
        if pass1 != pass2:
            return HttpResponse("Passwords do not match!")
        if not uname or not email or not pass1:
            return HttpResponse("All fields are required!")
        new_user = users(uname=uname, email=email, pass1=pass1)
        new_user.save()
        return render(request,'succ.html')

    return render(request, 'signup.html')

    

     
def login(request):
   if request.method == 'POST': 
        username = request.POST.get('username')
        password = request.POST.get('password')  
        Users = users.objects.filter(uname=username, pass1=password).first()
        if Users:
            return render(request,'home.html')  # Redirect to homepage after successful login
        else:
             error_message = "Username or Password is incorrect!"
             return render(request, 'login.html', {'error_message': error_message})
   return render(request, 'login.html')

