from charging_station.models import Charging_Station,Login
from charging_station.forms import UserRegisterForm,LoginForm
from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse
# from django.contrib.auth.decorators import login_required




def cs_home(request):
    cs_id=request.session.get('cs_id',None)
    try:
        if cs_id is not None:
            cs_info=Charging_Station.objects.get(id=cs_id)
            return render(request,"Charging_station/cs_home.html",{'cs_info':cs_info})
    except:
        return HttpResponse("please login to your account")