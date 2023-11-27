
from django.urls import path,include
from base import views

urlpatterns = [
    path("",views.index,name="index"),
    path("cs/",include("charging_station.urls")),


]
