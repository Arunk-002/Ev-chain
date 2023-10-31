from charging_station.models import Charging_Station,Login
from charging_station.forms import UserRegisterForm,LoginForm
from django.shortcuts import render, redirect



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

def cs_home(request):
    
    return render(request,"Charging_station/cs_home.html")