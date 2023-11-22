from django.shortcuts import render
# Create your views here.

def cshome(request):
    return render(request,"charging_station/cs_home.html")
