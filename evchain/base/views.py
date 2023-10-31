from charging_station.models import Charging_Station,Login
from charging_station.forms import UserRegisterForm,LoginForm
from django.shortcuts import render, redirect

# Create your views here.

def index(request):
    return render(request,"base/base.html")

def registration(request):
    if request.method=='POST':
        name=request.POST['name']
        email=request.POST['email']
        address=request.POST['place']
        phone=request.POST['phone']
        username=request.POST['username']
        password=request.POST['password']
        c_s=Charging_Station(name=name,address=address,phone=phone,email_id=email)
        login=Login(username=username,password=password)
        login.save()
        c_s.save()
        return redirect("login_page")
    return render(request,"base/registration.html")


def login_page(request):
    if request.method=='POST':
        form=LoginForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data['username']
            password=form.cleaned_data['password']
            try:
                if Login.objects.get(username=username,password=password):
                    return redirect('cshome')

            except Login.DoesNotExist:
                return render(request, 'base/login.html', {'form': form, 'error': 'Invalid credentials'})
            
        else:
            form=LoginForm()        
    return render(request,"base/login.html")

