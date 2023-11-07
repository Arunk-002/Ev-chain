from charging_station.models import Charging_Station,Login
from charging_station.forms import UserRegisterForm,LoginForm
from django.shortcuts import render, redirect
from django.contrib import messages

# Create your views here.

def index(request):
    return render(request,"base/index.html")

def registration(request):
    if request.method=='POST':
        name=request.POST['name']
        email=request.POST['email']
        address=request.POST['place']
        phone=request.POST['phone']
        username=request.POST['username']
        password=request.POST['password']
        c_s=Charging_Station(name=name,address=address,phone=phone,email_id=email)
        c_s.save()
        login=Login(username=username,password=password,cs_login=c_s)# saved the charging station object to the forien key cs_login in the login table
        login.save()
        
        return redirect("login_page")
    return render(request,"base/registration.html")


def login_page(request):
    if request.method=='POST':
        form=LoginForm(request.POST)#render out the loginform.
        if form.is_valid():#checking if the login form has valid data.
            username=form.cleaned_data['username']
            password=form.cleaned_data['password']
            #from the form saved the username and password to respective variables.
            try:
                cs_login_object=Login.objects.get(username=username,password=password)# retrieved the login object with corresponding ,
                # username and password and saved it to cs_login_object.
                loginObj_cs=cs_login_object.cs_login # accessed the corresponding Charging_station using the cs_login_object.
                if loginObj_cs and loginObj_cs.join_request=="Accept": # checked if the charging station is accepted or not
                    messages.add_message(request,messages.SUCCESS,"welocome Home")
                    return redirect('cshome')
                else:
                    messages.add_message(request,messages.WARNING,"Kindly wait your charging station is not verified")
            except Login.DoesNotExist:
                messages.add_message(request,messages.ERROR,"Check you Username and Password!!")
                return render(request, 'base/login.html', {'form': form})

        else:
            form=LoginForm()        
    return render(request,"base/login.html")

