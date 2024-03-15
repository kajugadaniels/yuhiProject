from django.shortcuts import render, redirect, HttpResponse
from .forms import SignUpForm, LoginForm
from django.contrib.auth import authenticate, login

def user_register(request):
    msg = None
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            msg = 'user created'
            return redirect('account:login')
        else:
            msg = 'form is not valid'
    else:
        form = SignUpForm()
        
    context = {
        'form': form,
        'msg': msg,
    }
    return render(request,'auth/register.html', context)

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
                return redirect('store:dashboard')
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

    pass