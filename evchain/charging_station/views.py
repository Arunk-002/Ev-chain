from django.shortcuts import render
from charging_station.models import *
# Create your views here.

def index(request):
    cs=Charging_Station.objects.all()
    context={'cs':cs}
    return render(request,"charging_station/base.html",context)
