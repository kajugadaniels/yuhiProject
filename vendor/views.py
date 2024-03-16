from django.shortcuts import render

def dashboard(request):
    return render(request, 'backend/vendor/dashboard.html')

def stockRecord(request):
r