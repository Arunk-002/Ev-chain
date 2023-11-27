from django.shortcuts import render,redirect
from charging_station.forms import ChargingStationSignupForm
from charging_station.models import Charging_Station
from base.models import BaseUser
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login
from django.contrib import messages
# Create your views here.


@login_required(redirect_field_name='cslogin')
def cshome(request):
    return render(request,"charging_station/cs_home.html")


def cs_registration(request):
    if request.method=='POST':
        address=request.POST['place']
        name=request.POST['name']
        email=request.POST['email']
        phone=request.POST['phone']
        username=request.POST['username']
        password=request.POST['password']
        user=BaseUser.objects.create_user(username=username,password=password,email=email,phone=phone,address=address)
        user.save()
        c_s = Charging_Station.objects.create(user=user, cmp_name=name, join_request='Reject', status='Unavailable')
        c_s.save()
        return redirect('cslogin')
    else:
        form = ChargingStationSignupForm()

    return render(request,"base/cs_registration.html",{'form':form})
def cs_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        cs = authenticate(request, username=username, password=password)
        print(cs)
        if cs is not None:
            if cs.is_staff:
                messages.add_message(request,messages.ERROR,"invalid user credentials")
            else:
                login(request, cs)
                messages.add_message(request,messages.SUCCESS,"welcome "+cs.username)
                return redirect('cshome') 
        else:
            messages.add_message(request,messages.ERROR,"invalid user credentials")
    return render(request, "base/cs_login.html")

