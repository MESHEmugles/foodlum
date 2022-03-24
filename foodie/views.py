import uuid
import requests
import json



from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.db.models import Q



from .models import *
from foodie.forms import *
from shopcart.forms import *
# from userprofile.forms import *

# Create your views here.


def index(request):
    # keys= Variety.objects.get(pk=id)
    # return HttpResponse('we are all foodie')
    breakfast= Meal.objects.filter(breakfast=True, display=True).order_by('-id')[:4]
    lunch= Meal.objects.filter(lunch=True, display=True).order_by('-id')[:4]
    dinner= Meal.objects.filter(dinner=True, display=True).order_by('-id')[:4]
    variety= Variety.objects.all()
    # profile = UProfile.objects.get(user__username= request.user.username)

    context={
        'breakfast':breakfast,
        'lunch':lunch,
        'dinner':dinner,
        'variety':variety,
        # 'profile':profile
    }

    return render(request, 'index.html', context)


def meals(request):
    mean= Meal.objects.all()
    # if 'itemsearch' in request.GET:
    #     searched = request.GET['itemsearch']
    #     mean = Meal.objects.filter(Q(Q(meal__icontains= searched)| Q(time__icontains=searched)))
    # else:
    #     mean= Meal.objects.all()

    context={
        'mean':mean,
    }
    return render(request, 'meals.html', context)

def searched(request):
    if request.method == 'POST':
        searched = request.POST['itemsearch']
        searched_item = Q(Q(meal__icontains=searched)| Q(time__icontains=searched))
        searched_meals = Meal.objects.filter(searched_item)
    else:
        searched_meals = Meal.objects.all()

    context={
        'searched_meals':searched_meals,
    }
    return render(request, 'searched.html', context)


def meal(request, id, slug):
    means= Meal.objects.get(pk=id)

    context={
        'means':means,
    }

    return render(request, 'meal.html', context)



def varieties(request, id, slug):
    varre= Meal.objects.filter(variety_id=id)
    vare= Variety.objects.get(pk=id)

    context={
        'varre':varre,
        'vare':vare,
    }

    return render(request, 'varieties.html', context)


def loggin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password1 = request.POST['password']
        user = authenticate(request, username= username , password=password1)
        if user:
            login(request, user)
            messages.success(request, 'Successful!')
            return redirect('index')
        else:
            messages.info(request, 'Not Successful!')
            return redirect('loggin')

    variety= Variety.objects.all()

    context={
        'variety':variety
    }
    
    return render(request, 'loggin.html', context)

def loggout(request):
    logout(request)
    return redirect('index')


def signup(request):
    form = SignupForm()  # instantiate the signupform for a Get request
    if request.method == 'POST': #check if a post method for persisting data to the DB
        phone = request.POST['phone']
        image = request.POST['image']
        form =SignupForm(request.POST) # instantiate the SignupFom for a POST request
        if form.is_valid(): #ensures security checks here
            user = form.save() #save data if data is valid
            newuser= UProfile( user = user)#field from the profile model # to automate user creation of account....newuser is representing the profile model
            newuser.first_name = user.first_name
            newuser.last_name = user.last_name
            newuser.phone = phone
            newuser.image = image
            newuser.save()
            login(request, user) #data of the user is passed into the login automatical
            messages.success(request, 'signup successful')
            return redirect('index') #send user into any page you desire in this case homepage
        else:
            messages.error(request, form.errors)
            return redirect('signup')
    
    context={
        'form':form,

    }
    return render(request, 'signup.html', context)


# authentication

def contactus(request):
    cform = ContactForm() #instantiate an empty form to GET request
    if request.method == 'POST':
        cform = ContactForm(request.POST) #instantiate request for a post request
        if cform.is_valid():
            cform.save()
            messages.success(request, 'Thank you for contacting us, our customer care will reach you soon')
            return redirect('index')
        else:
            messages.error(request, cform.errors)
            return redirect('index')
    
    
    context={
        'cform':cform
    }

    return render(request, 'contactus.html', context)


@login_required(login_url='loggin')
def profile(request):
    profile = UProfile.objects.get(user__username= request.user.username)

    context={
        'profile':profile,
    }
    
    return render(request, 'Profile.html', context)

@login_required(login_url='loggin')
def profileupdate(request):
    load_profile= UProfile.objects.get(user__username= request.user.username)
    form = ProfileForm(instance=request.user.uprofile)
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=request.user.uprofile)
        if form.is_valid():
            form=form.save()
            messages.success(request, f'Dear {form.first_name} your profile updates is successful')
            return redirect('profile')
        else:
            messages.error(request, f' Dear {form.first_name} kindly follow the following instructions {form.errors}, thank you.')
            return redirect('profile')

    context = {
        'load_profile': load_profile,
        'form':form,
    }
    return render(request, 'profileupdate.html', context)

@login_required(login_url='loggin')
def password_recovery(request):
    load_profile= UProfile.objects.get(user__username= request.user.username)
    form = PasswordChangeForm(request.user)
    if request.method == 'POST':
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Password Change Successful')
            return redirect('profile')
        else:
            messages.error(request, form.errors)
            return redirect('profile')

    context = {
        'load_profile':load_profile,
        'form':form
    }
    return render(request, 'password_recovery.html', context)

# cart
@login_required(login_url='loggin') 
def addtocart(request):
    # cart_code= str(uuid.uuid4())
    cartro = UProfile.objects.get(user__username = request.user.username)
    cart_code = cartro.cart_code
    if request.method == 'POST':
        addquantity = int(request.POST['quantity'])
        addspice = request.POST['now_spicy']
        addid = request.POST['mealid']
        mealid = Meal.objects.get(pk=addid)
        # instantiate the cart for prospertive users
        shopcart = Shopcart.objects.filter(user__username=request.user.username,item_paid=False)   #basket that's been stacked sonewhr 
        if shopcart:  #instantiate the cart for a selected item
            # more = Shopcart.objects.filter(meal_id= mealid.id, user__username= request.user.username).first() for incrementation method
            more = Shopcart.objects.filter(meal_id= mealid.id, quantity=addquantity, now_spicy=addspice, user__username= request.user.username).first()
            if more:
                more.quantity =addquantity
                more.now_spicy = addspice
                more.save()
                messages.success(request, 'Item has been added to your cart')
                return redirect('meals')  

            else: #create cart
                newcart = Shopcart()
                newcart.user=request.user
                newcart.meal = mealid
                newcart.quantity = addquantity
                newcart.now_spicy= addspice
                newcart.order_no= shopcart[0].order_no
                newcart.item_paid=False
                newcart.save()
                messages.success(request, 'Item has been added to your cart')
                return redirect('meals')
        else:
            newcart = Shopcart()
            newcart.user=request.user
            newcart.meal = mealid
            newcart.quantity = addquantity
            newcart.now_spicy= addspice
            newcart.order_no=cart_code
            newcart.item_paid=False
            newcart.save()
            messages.success(request, 'Item has been added to your cart')
            return redirect('meals')
    # return HttpResponse('add item to card')

@login_required(login_url='loggin') 
def cart(request):
    carty= Shopcart.objects.filter(user__username = request.user.username,item_paid=False)
    mean= Meal.objects.all()[:1]

    subtotal=0
    vat=0
    total= 0
    for item in carty:
        if item.meal.discount:
            subtotal += item.meal.discount + item.quantity
        else:
            subtotal += item.meal.price + item.quantity
    #vatis at 7.5% of the subtotal, that is 7.5/100 * subtotal
    vat = 0.075 * subtotal

    #addition of vat and subtotal gives the total value to be charged
    total= subtotal + vat
    context ={
        'mean':mean,
        'carty':carty,
        'subtotal':subtotal,
        'vat':vat,
        'total':total,
    }
    return render(request, 'cart.html', context)

@login_required(login_url='loggin') 
def remove_item(request):
    deleteitem = request.POST['deleteitem']
    Shopcart.objects.filter(pk=deleteitem).delete()
    messages.success(request, 'item successfully deleted from your shpcart')
    return redirect('meals')

# checkout
@login_required(login_url='loggin') 
def checkout(request):

    carty= Shopcart.objects.filter(user__username = request.user.username,item_paid=False)
    profile = UProfile.objects.get(user__username= request.user.username)

    subtotal=0
    vat=0
    total= 0
    for item in carty:
        if item.meal.discount:
            subtotal += item.meal.discount + item.quantity
        else:
            subtotal += item.meal.price + item.quantity
    #vatis at 7.5% of the subtotal, that is 7.5/100 * subtotal
    vat = 0.075 * subtotal

    #addition of vat and subtotal gives the total value to be charged
    total= subtotal + vat
    context ={
        'carty':carty,
        'subtotal':subtotal,
        # 'orderno':carty[0].order_no,
        'vat':vat,
        'total':total,
        'profile':profile,
    }
    return render(request, 'checkout.html', context)


@login_required(login_url='loggin') 
def paidorder(request):
    if request.method == 'POST':
        # collect data to sed to paystack
        # the api_key(application programming interface key) and curl(call url) will be sourced from paystack site
        # paystack will give test secret key for testing, when you want to g live paystack will give you live key
        # cburl
        api_key= 'sk_test_371cb1fe66df8f063548bf77f615d1a8c2411f24'
        curl= 'https://api.paystack.co/transaction/initialize'
        cburl = 'http://3.142.225.0/paid_order'
        # cburl = 'http://localhost:2000/paid_order'
        ref_num = str(uuid.uuid4())
        total= float(request.POST['get_total']) * 100
        # order_num= request.POST['get_orderno']
        address= request.POST['address']
        state= request.POST['state']
        phone= request.POST['phone']
        cartro = UProfile.objects.get(user__username = request.user.username)
        order_num = cartro.cart_code
        user= User.objects.get(username= request.user.username)

        headers= {'Authorization': f'Bearer {api_key}'}
        data = {'reference':ref_num, 'order_number': order_num, 'amount':int(total), 'callback_url':cburl, 'email':user.email, 'currency': 'NGN'}
        # collect data to send o paystack done

        # if curreny isn't stated the default is dollar

        # call to paystack
        try:
            r = requests.post(curl, headers=headers, json=data)
        except Exception:
            messages.error(request, 'network busy, pl refresh and try again. thank you.')
        else:
            transback = json.loads(r.text)
            rd_url = transback['data']['authorization_url']
            

            # take record of transaction made
            paidorder = Paidorder()
            paidorder.user = user
            paidorder.total = total/100
            paidorder.cart_no = order_num
            paidorder.payment_code = ref_num
            paidorder.paid_item =True
            paidorder.name_on_crd = user.first_name
            # paidorder.name_on_crd = user.first_name and user.last_name
            paidorder.save()


            ship =Ship()
            ship.user = user
            ship.total = total/100
            ship.phone = phone
            ship.state = state
            ship.address = address
            ship.ordr_no = order_num
            ship.itm_paid =True
            ship.name_on_crd = user.first_name
            ship.save()
            return redirect(rd_url)
        # call to paystack done, when transaction is successfull it redirects to the callback page
        # if transaction error occurs it rdirect us to the checkout
    # return redirect('checkout')



def paid_order(request):
    carty= Shopcart.objects.filter(user__username= request.user.username, item_paid=False)
    for item in carty:
        item.item_paid = True
        item.save()

    return render(request, 'paid_order.html')

