from django import forms
from vendor.models import Vendor

class EditProfileForm(forms.ModelForm):
    store_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter store name'}), required=True)
    manager_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter manager name'}), required=True)
    phone_number = forms.CharField(widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter phone number'}), required=True)
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter store email'}), required=True)
    address = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter store address'}), required=True)
    tin_number = forms.CharField(widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter phone number'}), required=True)
    image = forms.ImageField(required=True)
    
    class Meta:
        model = Vendor
        fields = ['store_name', 'manager_name', 'phone_number', 'email', 'address', 'tin_number', 'image']