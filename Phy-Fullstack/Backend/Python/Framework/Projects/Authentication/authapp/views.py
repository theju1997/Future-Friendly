from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib import auth
from django.contrib.auth.models import User

# Create your views here.
def home(request):
    return render(request,'home.html')

def user_registration(request):
    if request.method=='POST':
        first_name=request.POST.get('first_name')
        last_name=request.POST.get('last_name')
        user_name=request.POST.get('user_name')
        email=request.POST.get('email')
        mobile=request.POST.get('mobile')
        password1=request.POST.get('password1')
        password2=request.POST.get('password2')
        if password1==password2:
           if User.objects.filter(username=user_name).exists():
               messages.info(request,'username already taken')
               return redirect('user_registration')
           elif User.objects.filter(email=email).exists():
               messages.info(request,'email already taken')
               return redirect('user_registration')
           else:
               user=User.objects.create_user(first_name=first_name,
                                             last_name=last_name,
                                             username=user_name,
                                             password=password1,
                                             email=email
                                             )
               user.save()
              
               return redirect('login')
        else:
            return redirect('user_registration') 
        return redirect('/') 
    else:
        return render(request,'user_registration.html')

def login(request):
    if request.method=='POST':
        username=request.POST.get('user_name')   
        password=request.POST.get('password1')   
        print(username)
        print(password)
        user=auth.authenticate(username=username,password=password) 
        print(username)
        print(password)
        if user is not None:
            auth.login(request,user) 
            return redirect('/')   
        else:
            messages.info(request,'invalid credentials')
            return redirect('login')
    else:
        return render(request,'login.html')
    
def logout(request):
    auth.logout(request)
    return redirect('/')