import uuid 
from django.shortcuts import render, redirect, HttpResponse
from account.forms import SignUpForm, LoginForm
from vendor.models import Vendor
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

def user_register(request):
    msg = None
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            
            # Check if a vendor with the same phone number exists
            phone_number = form.cleaned_data['phone_number']
            existing_vendor = Vendor.objects.filter(phone_number=phone_number).first()
            if existing_vendor:
                msg = 'Vendor with this phone number already exists'
                # You can handle this case according to your requirements, like showing an error message or redirecting to a different page
            else:
                vid = uuid.uuid4()
                vendor = Vendor.objects.create(user=user, vid=vid)
                msg = 'User created'
                return redirect('account:login')
        else:
            msg = 'Form is not valid'
    else:
        form = SignUpForm()
        
    context = {
        'form': form,
        'msg': msg,
    }
    return render(request, 'auth/register.html', context)

def user_login(request):
    form = LoginForm(request.POST or None)
    msg = None
    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None and user.is_customer:
                login(request, user)
                return HttpResponse("This is the customer page")
            elif user is not None and user.is_vendor:
                login(request, user)
                return redirect('vendor:dashboard')
            else:
                msg= 'invalid credentials'
        else:
            msg = 'error validating form'
    
    context = {
        'form': form,
        'msg': msg,
    }
    return render(request, 'auth/login.html', context)

def user_logout(request):
    logout(request)
    messages.success(request, "You're logged out")
    return redirect("app:home")