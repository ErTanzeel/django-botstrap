from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login as auth_login,logout
import razorpay
from English.settings import RAZORPAY_API_KEY,RAZORPAY_API_SECRET_KEY

# Create your views here.
def Home(request):
    # video=Video.objects.all()
    return render(request,'home.html')

client = razorpay.Client(auth=(RAZORPAY_API_KEY,RAZORPAY_API_SECRET_KEY))  
def pay(request):
    order_amount = 50000
    order_currency = 'INR'

    payment_order = client.order.create(dict(amount=order_amount,currency=order_currency,payment_capture=1))
    payment_order_id = payment_order['id']
    context ={
        'amount':500,'api_key':RAZORPAY_API_KEY, 'order_id':payment_order_id

    }
    return render(request,'pay.html',context)

def about(request):
    return render(request,'about.html')  

def services(request):
    return render(request,'services.html')


def login(request):
    if request.method == "POST":
        username=request.POST['username']
        pass1=request.POST['pass1']

        user = authenticate(username=username, password=pass1)

        if user is not None:
            auth_login(request,user)
            fname = user.first_name
            return render(request,'home.html',{'fname': fname})
        else:
            messages.error(request,'bad credential')
            return redirect('login')

    return render(request,'login.html')   

def signup(request):
    if request.method =="POST":
        username=request.POST["username"]
        fname=request.POST["fname"]
        lname=request.POST["lname"]
        email=request.POST["email"]
        pass1=request.POST["pass1"]
        pass2=request.POST["pass2"]

        if User.objects.filter(username=username):
            messages.error(request,'username already exist please try another username')
            return redirect('Home')

        if User.objects.filter(email=email):
            messages.error(request,'Email already exists')
            return redirect("Home")

        if len(username)>10:
            messages.error(request,'username name limit exceed')

        if pass1 != pass2:
            messages.error(request,'password doesnot match')

        if not username.isalnum():
            messages.error(request,'username must be alphanumeric')
            return redirect('Home')

        
        newuser = User.objects.create_user(username, email, pass1)
        newuser.first_name = fname
        newuser.last_name = lname

        newuser.save()

        messages.success(request,'your account has been successfully created')

    return render(request,'contact.html') 

def signout(request):
    logout(request)
    messages.success(request,"logged out successfully")
    return render(request,'login.html') 



