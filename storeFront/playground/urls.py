from django.urls import path
from . import views

#URL Conf Module
urlpatterns = [
    path('hello/',views.say_hello,name = 'views.say_hello')
]