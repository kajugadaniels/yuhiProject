from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.contrib.auth import get_user_model
from vendor.models import Vendor
from vendor.forms import EditProfileForm

@login_required
def dashboard(request):
    return render(request, 'backend/vendor/dashboard.html')

@login_required
def profile(request, username):
    User = get_user_model()  # Get the custom user model
    user = User.objects.get(username=username)
    vendor, created = Vendor.objects.get_or_create(user=user)

    context = {
        'username': username,
        'vendor': vendor,
    }

    return render(request, 'backend/vendor/profile/index.html', context)

@login_required
def profileEdit(request, vid):
    vendor_instance, created = Vendor.objects.get_or_create(user=request.user)

    if request.method == 'POST':
        form = EditProfileForm(request.POST, request.FILES, instance=vendor_instance)
        if form.is_valid():
            form.save()
            return redirect(reverse('vendor:profile', kwargs={'username': request.user.username}))
    else:
        form = EditProfileForm(instance=vendor_instance)

    context = {
        'form': form,
    }
    return render(request, 'backend/vendor/profile/edit.html', context)

@login_required
def stockRecord(request):
    return render(request, 'backend/vendor/stock/index.html')

@login_required
def sellItem(request):
    return render(request, 'backend/vendor/sellItem/index.html')
