from django.db import models
from django.core.validators import RegexValidator

#status choices 
status_choice=(
    ('Available','Available'),
    ('Unavailable','Unavailable'),
)
#regx validators
regx_phone=RegexValidator(
    regex="^(\+91[\-\s]?)?[0]?(91)?[789]\d{9}$",
    message="Phone number must be exactly 10 digits long (e.g., 1234567890)."
    )
#this ensures that the user can input only 10 digits and it will be digits rather than text   

class Charging_Station(models.Model):
   
    name=models.CharField(blank=False,max_length=50)
    place=models.CharField(blank=False,max_length=100)
    phone = models.CharField(blank=False,max_length=10,validators=[regx_phone])
    email_id=models.EmailField(blank=False)
    status=models.CharField(blank=False,choices=status_choice, max_length=20,default='None')

    def __str__(self):
        return self.name