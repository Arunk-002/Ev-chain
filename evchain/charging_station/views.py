from django.shortcuts import render,redirect
from charging_station.forms import ChargingStationSignupForm
from charging_station.models import Charging_Station
from base.models import BaseUser
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login
from django.contrib import messages
# Create your views here.


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
        if cs is not None:
            if cs.is_staff:
                messages.add_message(request,messages.ERROR,"invalid user credentials")
            else:
                cs_id=Charging_Station.objects.get(user=cs)
                if cs_id.join_request=="Accept":
                    login(request, cs)
                    messages.add_message(request,messages.SUCCESS,"welcome "+cs_id.cmp_name)
                    return redirect('cshome',cs.pk) 
                else:
                    messages.add_message(request,messages.ERROR,"Join request is not yet accepted")
                    return redirect('cslogin')
        else:
            messages.add_message(request,messages.ERROR,"invalid user credentials")
    return render(request, "base/cs_login.html")



@login_required(redirect_field_name='cslogin')
def cshome(request,cs):
    if cs is not None:
        base_cs_info=BaseUser.objects.get(id=cs)
        cs_info=Charging_Station.objects.get(user=cs)
        context={'base_cs_info':base_cs_info,
                 'cs_info':cs_info}
        if request.method == 'POST':
            status_value = request.POST.get('status')
            cs_info.status=status_value
    
    return render(request,"charging_station/cs_home.html",context)
