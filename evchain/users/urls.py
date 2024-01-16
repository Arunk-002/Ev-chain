from django.urls import path
from users import views

urlpatterns=[
    path("<int:user>/",views.userHome,name="userhome"),
    path("reg/",views.userRegistration,name="userreg"),
    path("login/",views.userLogin,name="userlogin"),
    path("profile/",views.profileUpdate,name="userprofile"),
    path("booking/<int:cs_id>/",views.userBooking,name="userbooking"),
]