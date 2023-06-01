from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from .models import Apartment

def signup(request):
    if request.method=='POST':
        uname = request.POST['username']
        email=request.POST['email']
        pass1 = request.POST['password1']
        cpass1=request.POST['password2']

        if pass1!=cpass1:
            return HttpResponse('password and confirm password are not same')

        else:
            myuser = User.objects.create_user(uname,email,pass1)
        myuser.save()
        return redirect('login')
        
    return render(request,'signup.html')
def Login(request):
    if request.method=='POST':
        username=request.POST['username']
        pass1=request.POST['pass']
        user = authenticate(request,username=username,password=pass1)

        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            return HttpResponse('Username and password is incorrect!!!')

    return render(request,'login.html')

def Logoutpage(request):
    logout(request)
    return redirect('login')


def Home(request):
    upload=Apartment.objects.all()
    return render(request,'home.html',{'upload':upload})

def send_template_email(request):
    subject='this is the demo for sending email'
    plain_message='hey, just completed email integration on django'
    from_email='abinashpoudel54321@gmail.com'
    to_email=['abinashnew24@gmail.com']
    send_mail(subject, plain_message, from_email, to_email)
    return HttpResponse('email sent successfully')

def Contact(request):
    return render(request,'contact.html')
def About(request):
    return render(request,'about.html')
