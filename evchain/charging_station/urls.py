from django.urls import path
from charging_station import views
urlpatterns = [
    path("",views.cshome ,name="cshome")
]
