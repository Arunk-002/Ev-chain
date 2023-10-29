from charging_station.models import Charging_Station
from charging_station.forms import UserRegisterForm
from django.shortcuts import render, redirect

def index(request):
    cs=Charging_Station.objects.all()
    context={'cs':cs}
    return render(request,"Charging_station/base.html",context)

# def registration(request):
#     if request.method=='POST':
#         form=UserRegisterForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect(index)
#     else:
#         form=UserRegisterForm()
#     context={'form':form}
#     return render(request,"Charging_station/registration.html",context)
def registration(request):
    if request.method=='POST':
        name=request.POST['name']
        email=request.POST['email']
        place=request.POST['place']
        phone=request.POST['phone']
        status=request.POST['status']
        c_s=Charging_Station(name=name,place=place,phone=phone,email_id=email,status=status)
        c_s.save()
    return render(request,"Charging_station/registration.html")