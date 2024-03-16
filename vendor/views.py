from django.shortcuts import render

def dashboard(request):
    return render(request, 'backend/vendor/dashboard.html')

def stockRecord(request):
    return render(request, 'backend/vendor/stock/index.html')

def sellItem(request):
    return render(request, 'backend/vendor/sellItem/index.html')
