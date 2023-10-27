from charging_station.models import Charging_Station
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

def index(request):
    cs=Charging_Station.objects.all()
    context={'cs':cs}
    return render(request,"Charging_station/base.html",context)

def registration(request):
    if request.method=='POST':
        form=UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(index)
    else:
        form=UserCreationForm()
    context={'form':form}
    return render(request,"Charging_station/registration.html",context)