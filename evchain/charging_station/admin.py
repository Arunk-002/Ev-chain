from django.contrib import admin
from charging_station.models import Charging_Station,Cs_Offers

# Register your models here.
admin.site.register(Charging_Station)
admin.site.register(Cs_Offers)