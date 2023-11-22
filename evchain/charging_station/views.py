from django.shortcuts import render,redirect
from charging_station.forms import ChargingStationForm
from charging_station.models import Charging_station
# Create your views here.

def cshome(request):
    return render(request,"charging_station/cs_home.html")
def cs_registration(request):
    if request.method=='POST':
        name=request.POST['name']
        address=request.POST['place']
        phone=request.POST['phone']
        username=request.POST['username']
        password=request.POST['password']
        c_s=Charging_station(cmp_name=name,address=address,phone=phone,username=username,password=password)
        c_s.save()
        return redirect('cshome')
    else:
        form = ChargingStationForm()

    return render(request,"base/cs_registration.html",{'form': form})