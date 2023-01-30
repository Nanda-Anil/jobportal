from django.urls import path
from .views import *

urlpatterns=[
    path('index/',index),
    path('log/',Login),
    path('register/',Register),
    # path('navbar/',Nav),
    # path('footer/',foot)
    path('profile/',profile),
    path('aboutus/',aboutus),



    path('uploadvacancies/<int:id>',uploadview),
    path('vacancydisplay/',displayview),
    path('deletevacancy/<int:id>',deletevacancy),
    path('editvacancy/<int:id>',editvacancy),

    path('userregister/',UserRegister.as_view(),name='userregister'),
    path('userlog/',UserLogin.as_view(),name='userlog'),


    path('profileuser/',profileuser,name='profileuser'),
    path('profiledetails/',profile_details),
    path('userprofiledis/',userprodis),
    path('vacancyview/',vacancyview),
    path('apply/<int:id>',userapply),
    # path('userapply/',userapply),
    path('emailalert/',emailalert),
    path('wishlist/<int:id>',wishlist),
    path('wishdetail/',wishdetail),
    path('removewish/<int:id>',removewish),

    path('appliedusers/',appliedusersdisplay),
    path('removeuser/<int:id>',removeuser),
    path('sendemail/<int:id>',sendemail),


]