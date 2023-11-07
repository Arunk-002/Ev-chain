from django.urls import path
from charging_station import views
urlpatterns = [
    path("cshome/",views.cs_home ,name="cshome"),
]
