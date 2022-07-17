from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('blockchain', views.blockchain, name='blockchain'),
    path('officerlogin', views.officerlogin, name='officerlogin'),
    path('registration_page', views.registration_page, name='registration_page'),
    path('aboutus', views.aboutus, name='aboutus'),
    path('contactus', views.contactus, name='contactus'),
    path('success', views.success,name="success"),
    path('sendmail', views.sendmail, name='sendmail'),
    path('marketplace', views.marketplace, name="marketplace")
]
