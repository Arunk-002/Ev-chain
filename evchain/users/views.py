from django.shortcuts import render,redirect
from base.models import BaseUser
from users.models import Custom_User
from charging_station.models import Cs_Offers,Charging_Station
from django.contrib.auth import authenticate,login
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required(redirect_field_name='userlogin')
def userHome(request,user):
    if user is not None:
        ev_stations=Charging_Station.objects.filter(status='Available')
        offers=Cs_Offers.objects.all()
        current_user_obj=BaseUser.objects.get(id=user)
        current_user=Custom_User.objects.get( C_user=user)
        context={
            'Customuser':current_user,
            'Baseuser':current_user_obj,
            'offers':offers,
            'stations':ev_stations,
        }
        return render(request,'users/user_home.html',context)
    else:
        return redirect('userlogin')
@login_required(redirect_field_name='userlogin')  
def profileUpdate(request):
    current_user=Custom_User.objects.get(C_user_id=request.user)
    if request.method=='POST':
        Place=request.POST['place']
        Vehicle=request.POST['vehicle']
        vehicle_no=request.POST['vehicleno']
        image=request.POST['image']
        current_user.place=Place
        current_user.vehicle_type=Vehicle
        current_user.vehicle_no=vehicle_no
        current_user.user_img=image
        current_user.save()
        messages.add_message(request,messages.SUCCESS,"welcome")    
    return render(request,'users/user_profile.html',{'Customuser':current_user})

def userRegistration(request):
    if request.method == 'POST':
        username=request.POST['username']
        password=request.POST['password']
        email=request.POST['email']
        phone=request.POST['phone']
        name=request.POST['name']
        place=request.POST['Place']
        age=request.POST['age']
        address=request.POST['address']
        vehicle=request.POST['vehicle']
        vehicle_no=request.POST['vehicleno']
        image=request.POST['image']
        userobj=BaseUser.objects.create_user(username=username,password=password,email=email,phone=phone,address=address)
        # when creating a user table object always use '.create_user' else when saving the password will not be hashed
        userobj.save()
        user=Custom_User.objects.create(C_user=userobj,name=name,place=place,age=age,
                                        vehicle_type=vehicle,vehicle_no=vehicle_no,user_img=image)
        user.save()
        return redirect('userlogin')
        
    return render(request,'users/user_registration.html')

def userLogin(request):
    if request.method == 'POST':
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(request,username=username,password=password)
        if user is not None:
            if user.is_staff:
                messages.add_message(request,messages.ERROR,"invalid user credentials")
            else:
                login(request,user)
                messages.add_message(request,messages.SUCCESS,"welcome")
                return redirect('userhome',user.pk)
                    
        else:
            messages.add_message(request,messages.ERROR,"invalid user credentials")

    return render(request,'users/user_login.html')

def userBooking(request,cs_id):
    cs=Charging_Station.objects.get(pk=cs_id)
    return render(request,'users/user_booking.html',{'cs':cs})