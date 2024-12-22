from django.urls import path
from.views import *
urlpatterns=[
    path('',base,name='base'),
    path('home/',home,name='home'),
    path('menu/',menu,name='menu'),
    path('about/',about,name='about'),
    path('contact/',contact,name='contact'),
]