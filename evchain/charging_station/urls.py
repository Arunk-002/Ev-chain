from django.urls import path
from charging_station import views
urlpatterns = [
    path("",views.index ,name="index"),
    path("register/",views.registration ,name="registration"),
]
