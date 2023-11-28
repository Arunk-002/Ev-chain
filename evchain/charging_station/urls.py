from django.urls import path
from charging_station import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path("<int:cs>/",login_required(views.cshome) ,name="cshome"),
    path("csreg/",views.cs_registration ,name="csregistration"),
    path("cslog/",views.cs_login ,name="cslogin"),
    
]
