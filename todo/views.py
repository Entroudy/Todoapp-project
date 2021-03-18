from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login, logout, authenticate
from django.views.decorators.csrf import csrf_exempt

def home(request):
    return render(request, 'todo/home.html')


@csrf_exempt
def signupuser(request):
    if request.method == 'GET':
        return render(request, 'todo/signupuser.html', {'form':UserCreationForm()})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('currenttodos')
            except IntegrityError:
                return render(request, 'todo/signupuser.html', {'form':UserCreationForm(), 'error':'This username has already been taken!'})
        else:
            return render(request, 'todo/signupuser.html', {'form':UserCreationForm(), 'error':'The Passwords did not match'})

        
def loginuser(request):
    if request.method == 'GET':
        return render(request, 'todo/loginuser.html', {'form':AuthenticationForm()})
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'todo/loginuser.html', {'form':AuthenticationForm(), 'error':'Username and Password did not match!'})
        else:
            login(request, user)
            return redirect('currenttodos')
        
        
def logoutuser(request):
    if request.method == 'POST':
        logout(request)
        return redirect('home')
        
        
def currenttodos(request):
    return render(request, 'todo/currenttodos.html')
    
    
    
    
    
    
    
    
    
    
    
    
    
    