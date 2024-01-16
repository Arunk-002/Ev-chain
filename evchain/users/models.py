from django.db import models
from base.models import BaseUser

# Create your models here.
vehicles=(
    ('Four wheeler','Four wheeler'),
    ('Two wheeler','Two wheeler')
)

class Custom_User(models.Model):
    C_user = models.OneToOneField(BaseUser, on_delete=models.CASCADE, primary_key=True)
    name=models.CharField(blank=False,max_length=150)
    place=models.CharField(blank=False,max_length=150)
    age=models.IntegerField(blank=False)
    vehicle_type=models.CharField(blank=False,choices=vehicles,max_length=100)
    vehicle_no=models.CharField(blank=False,max_length=150)
    user_img=models.ImageField(default='default.jpg',upload_to='user_images/')
    def __str__(self):
        return self.name