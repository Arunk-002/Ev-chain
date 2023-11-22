from django.db import models
from django.contrib.auth.models import AbstractUser
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

class Charging_station(AbstractUser):
    status=models.CharField(blank=False,choices=status_choice, max_length=20)
    join_request=models.CharField(blank=False,choices=j_request, max_length=20)
    address=models.CharField(max_length=200,blank=False)
    groups=None
    user_permissions=None
    def save(self,*args,**kwargs):
        if not self.pk:
            self.role=self.base_role
            return super().save(*args,**kwargs)