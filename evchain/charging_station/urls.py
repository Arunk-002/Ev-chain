from django.urls import path
from charging_station import views
urlpatterns = [
    path("",views.index ,name="index"),
    path("register/",views.registration ,name="registration"),
    path("login/",views.login_page ,name="login_page"),
    path("cshome/",views.cs_home ,name="cshome"),
]
