from django.db import models
from django.core.validators import RegexValidator,MinLengthValidator
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
#regx validators
regx_password=RegexValidator(
    regex="^(?=.*[A-Z])(?=.*[\W_]).{8,}$"
)
regx_phone=RegexValidator(
    regex="^(\+91[\-\s]?)?[0]?(91)?[789]\d{9}$"
    )
#this ensures that the user can input only 10 digits and it will be digits rather than text   

class Charging_Station(models.Model):
    name=models.CharField(blank=False,max_length=50)
    address = models.TextField(blank=False, max_length=100, default='Your_Default_Value')
    phone = models.CharField(blank=False,max_length=10,validators=[regx_phone])
    email_id=models.EmailField(blank=False)
    status=models.CharField(blank=False,choices=status_choice, max_length=20,default='None')
    join_request=models.CharField(blank=False,choices=j_request, max_length=20,default='None')

    def __str__(self):
        return "new request:"+self.name
    
class Login(models.Model):
    username=models.CharField(blank=False,max_length=15)
    password=models.CharField(blank=False,validators=[MinLengthValidator(8),regx_password],max_length=15)
    cs_login=models.OneToOneField(Charging_Station,on_delete=models.CASCADE,null=True, blank=True)

    
