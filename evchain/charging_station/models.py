from django.db import models
from base.models import BaseUser
from PIL import Image

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
    cs_Img=models.ImageField(default='default.jpg',upload_to="cs_images/")
    
    def __str__(self):
        return self.cmp_name
            
class Cs_Offers(models.Model):
    cs=models.ForeignKey(Charging_Station, on_delete=models.CASCADE)
    offer=models.CharField(max_length=300,blank=False)
    offer_post_day=models.DateTimeField(auto_now_add=True)
    offer_duration=models.DateField()
    offer_price=models.DecimalField(max_digits=10,decimal_places=2)

    def __str__(self):
        return self.offer


