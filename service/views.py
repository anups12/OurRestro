import json
from django.http import JsonResponse
from django.shortcuts import render, redirect
from . forms import AddNewProduct, UserCreate
from . models import *
from django.contrib.auth import logout, login, authenticate
from win10toast import ToastNotifier


# Create your views here.
def Message(request):
    data = json.loads(request.body)
    user = data['user']
    hr=ToastNotifier()
    hr.show_toast("Notification", f" Hello {user} You are inactive for 5 minutes")
    return JsonResponse('Data added successfully', safe=False)


def Home(request):
    product = Dishes.objects.all()
    if request.user.is_authenticated:
        cart = Cart.objects.filter(customer=request.user.customer)[::-1]
        cart_total=0
        for p in cart:
            cart_total+=p.total_price
    else:
        cart={}
        cart_total=0

    context={'product':product, 'cart':cart, 'cart_total':cart_total}
    return render(request, 'index.html', context)


def AddProduct(request):
    form = AddNewProduct()
    if request.method=='POST':
        product= AddNewProduct(request.POST)
        if product.is_valid():
            product.save()
    context={'form':form}
    return render(request, 'add.html', context)

def Register(request):
    form = UserCreate()
    if request.method=='POST':
        print(request.POST)
        form = UserCreate(request.POST)
        if form.is_valid():
            user = form.save()
            Customer.objects.create(user=user, name=user.username)
            return redirect('/')
    context={'form':form}
    return render(request, 'register.html', context)


def UserLogin(request): 
    form=UserCreate()
    if request.user.is_authenticated:
        return redirect('/')
    else:
        if request.method=='POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user) 
                return redirect('/')
    return render(request, 'register.html', {'form':form})

def UserLogout(request):
    logout(request)
    return redirect('/register/')

def AddToCart(request):
    data = json.loads(request.body)
    id = data['productId']
    action = data['action'] 
    dish= Dishes.objects.get(id=id)
    customer= request.user.customer
    cart, created = Cart.objects.get_or_create(customer=customer, dish=dish)
    if action =='add':
        cart.quantity +=1
    elif action == 'remove':
        cart.quantity -=1
    cart.save()
    if cart.quantity<=0:
        cart.delete()
    return JsonResponse('Data added successfully', safe=False)