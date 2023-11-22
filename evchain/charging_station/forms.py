from django import forms
from .models import Charging_station

class ChargingStationForm(forms.ModelForm):
    class Meta:
        model = Charging_station
        fields = ['username', 'password', 'cmp_name', 'email', 'address', 'phone', 'status', 'join_request']
