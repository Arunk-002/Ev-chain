from django import forms
from .models import Charging_Station
from base.models import BaseUser

class ChargingStationSignupForm(forms.ModelForm):
    username=forms.CharField(max_length=55, required=True)
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Charging_Station
        fields = ['cmp_name', 'join_request', 'status']

    # Add additional fields if needed, like address, name, email, and phone
    address = forms.CharField(max_length=200, required=True)
    name = forms.CharField(max_length=255, required=True)
    email = forms.EmailField(required=True)
    phone = forms.CharField(max_length=10, required=True)