from django.contrib import auth
from django.shortcuts import redirect
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import *
from .models import *

"""<-------APIView method for serializer---start-------->"""

"""<----------for manually token generation---start--->"""
from rest_framework_simplejwt.tokens import RefreshToken


class RegisterAPI(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if not serializer.is_valid():
            print(serializer.errors)
            return Response({'status': 403, 'errors': serializer.errors, 'message': 'something went wrong'})
        serializer.save()

        user = User.objects.get(username=serializer.data['username'])
        refresh = RefreshToken.for_user(user)

        return Response(
            {'status': 200, 'payload': serializer.data, 'refresh': str(refresh), 'access': str(refresh.access_token),
             'message': 'your data is save'})


"""<----------for manually token generation---end--->"""

from rest_framework_simplejwt.authentication import JWTAuthentication


class productAPI(APIView):
    authentication_classes = [JWTAuthentication]

    def get(self, request):
        queryset = product.objects.all()
        serializer = productSerializer(queryset, many=True)
        print(request.user)
        return Response({'status': 200, 'payload': serializer.data})

    def post(self, request):
        serializer = productSerializer(data=request.data)
        if not serializer.is_valid():
            print(serializer.errors)
            return Response({'status': 403, 'errors': serializer.errors, 'message': 'something went wrong'})
        serializer.save()
        return Response({'status': 200, 'payload': serializer.data, 'message': 'your data is save'})

    def patch(self, request):
        try:
            stu_obj = product.objects.get(id=request.data['id'])
            serializer = productSerializer(stu_obj, data=request.data, partial=True)
            if not serializer.is_valid():
                print(serializer.errors)
                return Response({'status': 403, 'errors': serializer.errors, 'message': 'something went wrong'})
            serializer.save()
            return Response({'status': 200, 'payload': serializer.data, 'message': 'your data is save'})
        except Exception as e:
            print(e)
            return Response({'status': 403, 'message': 'you have entered invalid id'})

    def put(self, request):
        try:
            stu_obj = product.objects.get(id=request.data['id'])
            serializer = productSerializer(stu_obj, data=request.data, partial=False)
            if not serializer.is_valid():
                print(serializer.errors)
                return Response({'status': 403, 'errors': serializer.errors, 'message': 'something went wrong'})
            serializer.save()
            return Response({'status': 200, 'payload': serializer.data, 'message': 'your data is save'})
        except Exception as e:
            print(e)
            return Response({'status': 403, 'message': 'you have entered invalid id'})

    def delete(self, request):
        try:
            id = request.GET.get('id')
            stu_obj = product.objects.get(id=id)
            stu_obj.delete()
            return Response({'status': 200, 'message': 'deleted'})

        except Exception as e:
            print(e)
            return Response({'status': 403, 'message': 'you have entered invalid id'})



"""<-------APIView method for serializer------end----->"""


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
        