from django.urls import path
from charging_station import views
urlpatterns = [
    path("",views.cshome ,name="cshome"),
    path("csreg/",views.cs_registration ,name="csregistration"),
    path("cslog/",views.cs_login ,name="cslogin"),
    
]
