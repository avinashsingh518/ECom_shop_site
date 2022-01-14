
# Create your views here.

from django.contrib import auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from .models import product, Contact, Cloth


def home(request):
    return render(request, 'index.html')

def index(request):
    p = Cloth.objects.all()
    return render(request,'index.html', {'p':p })

def shop(request):
    return render(request, 'categories.html')

def check_out(request):
    return render(request, 'check_out.html')

def blog(request):
    return render(request, 'check_out.html')

def product_page(request):
    h=product.objects.all()
    return render(request, 'product_page.html', {'h':h })

def about(request):
     return render(request, 'product_page.html')

def shopping_cart(request):
    return render(request,'shopping_cart.html')

def contact(request):
    c=Contact.objects.all()
    return render(request, 'contact.html', {'c': c} )


def signup(request):
    if request.method=='POST':
        username=request.POST['username']
        firstname= request.POST['first_name']
        lastname = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        x=User.objects.create_user(username=username,first_name=firstname,last_name=lastname,email=email,password=password)
        x.save()
        print("user created successfully")
        return redirect("/")
    else:
        return render(request,'signup.html')


def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
    
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            return redirect('login')
    else:
        return render(request, 'login.html')

def logout(request):
    auth.logout(request)
    return redirect('/')

def query(request):
    if request.method=='POST':
        firstname= request.POST['first_name']
        lastname = request.POST['last_name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']
        x=User.objects.create_user(first_name=firstname,last_name=lastname,email=email,message=message,subject=subject)
        x.save()
        print("we have taken your message successfully")
        return redirect('/')
    else:
        return render(request,'contact.html')
        