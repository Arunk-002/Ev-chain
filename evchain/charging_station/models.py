from django.db import models
from django.contrib.auth.models import AbstractUser
from base.models import BaseUser

# Create your models here.
#join request 
j_request=(
    ('Reject','Reject'),
    ('Accept','Accept'),
    
)
#status choices 
status_choice=(
    ('Available','Available'),
    ('Unavailable','Unavailable'),
)

class Charging_Station(models.Model):
    user = models.OneToOneField(BaseUser, on_delete=models.CASCADE, primary_key=True)
    cmp_name = models.CharField(max_length=255)
    join_request = models.CharField(max_length=60,choices=j_request,default='Reject')
    status = models.CharField(max_length=50,choices=status_choice,default='Unavailable')
    
    def __str__(self):
        return self.cmp_name