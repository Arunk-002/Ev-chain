from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
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

regx_phone=RegexValidator(
    regex="^(\+91[\-\s]?)?[0]?(91)?[789]\d{9}$"
    )

class Charging_station(AbstractUser):
    cmp_name=models.CharField(blank=False,max_length=50,default=None)
    phone = models.CharField(blank=False,max_length=10,validators=[regx_phone],default=None)
    status=models.CharField(blank=False,choices=status_choice, max_length=20)
    join_request=models.CharField(blank=False,choices=j_request, max_length=20)
    address=models.CharField(max_length=200,blank=False)
    groups=None
    user_permissions=None
