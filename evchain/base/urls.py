from django.urls import path,include
from base import views
urlpatterns = [
    path("",views.index ,name="index"),
    path("cs/",include("charging_station.urls")),
    path("register/",views.registration ,name="registration"),
    path("login/",views.login_page ,name="login_page"),

]
